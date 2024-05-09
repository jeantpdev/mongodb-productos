from librerias import *
from dotenv import load_dotenv
load_dotenv()

class Formulario():        

    def eliminar_imagen(self):

        id_producto = request.json['id']
        imagen_url = request.json['imagen_url']
        tipo_imagen = request.json['tipo_imagen']
        index = request.json['index']

        parts = imagen_url.split('/')
        imagen_id = parts[-1].split('.')[0]

        try:
            cloudinary.config( 
                cloud_name = os.getenv('CLOUD_NAME'), 
                api_key = os.getenv('API_KEY'), 
                api_secret = os.getenv('API_SECRET'))

            res = cloudinary.uploader.destroy(imagen_id)

            imagen_eliminada = res['result']

            if imagen_eliminada == "ok":
                client = MongoClient(os.getenv('MONGO_URI'))
                db = client.Productos

                if tipo_imagen == "principal":
                    db.lista_productos.update_one(
                        {"_id": id_producto},
                        {"$set": {"imagen_principal": "no dado"}})

                if tipo_imagen == "secundaria":
                    producto = db.lista_productos.find_one({"_id": id_producto})
                    if producto:
                        imagen_a_eliminar = producto["imagenes_productos"][index]
                        db.lista_productos.update_one(
                            {"_id": id_producto},
                            {"$pull": {"imagenes_productos": imagen_a_eliminar}})

                producto_actualizado = db.lista_productos.find_one({"_id": id_producto})
                print(producto_actualizado)

                return jsonify({"status_imagen_eliminada": "correcto"}), 200

        except Exception as e:
            print(e)
            return jsonify({"status_imagen_eliminada": "error"})
        
    def crear_imagen(self):

        try:

            cloudinary.config( 
            cloud_name = os.getenv('CLOUD_NAME'), 
            api_key = os.getenv('API_KEY'), 
            api_secret = os.getenv('API_SECRET'))
        
            imagen_principal = request.files.getlist('imagen_principal')
            imagenes_secundarias = request.files.getlist('imagenes_secundarias')

            # Se sube imagen principal
            resultado = cloudinary.uploader.upload(imagen_principal[0])
            url_imagen_principal = resultado['secure_url']

            urls_imagenes_secundarias = []
            for imagen in imagenes_secundarias:
                resultado = cloudinary.uploader.upload(imagen)
                url_imagen = resultado['secure_url']
                urls_imagenes_secundarias.append(url_imagen)

            return jsonify({"urls_imagenes_secundarias": urls_imagenes_secundarias, "url_imagen_principal": url_imagen_principal})
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500     
        
    def insertar_producto(self):

        client = MongoClient(os.getenv('MONGO_URI'))
        db = client.Productos

        id = request.json['_id']
        nombre = request.json['nombre_producto']
        categoria = request.json['categoria']
        descripcion = request.json['descripcion']
        precio = int(request.json['precio'])
        descuento = int(request.json['descuento'])
        imagen_principal = request.json['imagen_principal']
        imagenes_productos = request.json['imagenes_productos']
        dimensiones = request.json['dimensiones']
        material = request.json['material']

        documento = {
            "_id": id,
            "nombre_producto": nombre,
            "categoria": categoria,
            "descripcion": descripcion,
            "precio": precio,
            "descuento": descuento,
            "imagen_principal": imagen_principal,
            "imagenes_productos": imagenes_productos,
            "dimensiones": dimensiones,
            "material": material
        }
        
        db.lista_productos.insert_one(documento)
        
        return jsonify({"mensaje": "Producto insertado correctamente"})

    # FALTA ACTUALIZAR LA IMAGEN EN LA BD
    def guardar_imagen(self):

        client = MongoClient(os.getenv('MONGO_URI'))
        db = client.Productos

        cloudinary.config( 
            cloud_name = os.getenv('CLOUD_NAME'), 
            api_key = os.getenv('API_KEY'), 
            api_secret = os.getenv('API_SECRET'))
        
        try:
            imagenes = request.files.getlist('imagenes')
            tipo_imagen = request.form.get('tipo_imagen')
            if tipo_imagen == "imagen principal":
                id = request.form.get('id')

            urls_imagenes = []
            
            for imagen in imagenes:
                resultado = cloudinary.uploader.upload(imagen)
                url_imagen = resultado['secure_url']
                urls_imagenes.append(url_imagen)

            print(urls_imagenes)

            if tipo_imagen == "imagen principal":
                print("entre a imagen principal")
                db.lista_productos.update_many(
                {"_id": id},
                {"$set": {"imagen_principal": urls_imagenes[0]}})
                print("imagen principal actualizada")
                return jsonify({"urls_imagenes": urls_imagenes})
            
            if tipo_imagen == "imagenes secundarias":
                print("entre a imagen secundarias")
                db.lista_productos.update_one(
                    {"_id": id},
                    {"$addToSet": {"imagenes_productos": {"$each": urls_imagenes}}}
                )
                print("Imagenes secundarias agregadas o actualizadas")
                return jsonify({"urls_imagenes": urls_imagenes})
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def get_productos(self):
        client = MongoClient(os.getenv('MONGO_URI'))
        db = client.Productos
        
        lista_productos = db.lista_productos.find()
        datos = []

        for producto in lista_productos:
            datos.append(producto)
        
        return jsonify({"productos": datos})
    
    def editar_campo_producto(self):

        client = MongoClient(os.getenv('MONGO_URI'))
        db = client.Productos

        id = str(request.json['_id'])
        nombre_producto = request.json['nombre_producto']
        categoria = request.json['categoria']
        precio = int(request.json['precio'])
        descripcion = request.json['descripcion']

        info_producto_editar = {
            "nombre_producto": nombre_producto,
            "categoria": categoria,
            "descripcion": descripcion,
            "precio": precio
        }

        db.lista_productos.update_many(
            {"_id": id},
            {"$set": info_producto_editar})

        return jsonify({"mensaje": "Producto actualizado correctamente"})
    
    def eliminar_producto(self, id_producto):
        client = MongoClient(os.getenv('MONGO_URI'))
        db = client.Productos

        id = str(id_producto)

        resultado = db.lista_productos.delete_one({"_id": id})

        if resultado.deleted_count == 1:
            return jsonify({"mensaje": "Producto eliminado correctamente"})
        else:
            return jsonify({"mensaje": "No se encontró ningún producto con el ID especificado"})