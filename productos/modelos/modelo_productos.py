from librerias import *
from conexiones.conexionMongoDB import mongo
from conexiones.conexionCloudinary import cloudinary_bd
from utils import *

class Formulario():  

    #TODO: Recibir busqueda de columan en especifico
    def eliminar_imagen(self):
        id_producto = request.json['id']
        producto = mongo.buscar_producto(id_producto)

        if producto:
            imagen_url = request.json['imagen_url']
            tipo_imagen = request.json['tipo_imagen']
            index = request.json['index']
            id_imagen = utils.extraer_id_imagen(imagen_url)

            try:
                imagen_eliminada = cloudinary_bd.eliminar_imagen(id_imagen)

                if imagen_eliminada == "ok":

                    if tipo_imagen == "principal":
                        resultado = mongo.actualizar_imagen_principal(id_producto, "no dado")

                        if resultado == "actualizada":
                            return jsonify({"status_imagen_eliminada": "correcto", "mensaje": "Imagen eliminada"}), 200
                        else:
                            return jsonify({"mensaje": "Error al eliminar imagen"}), 500       
            
                    if tipo_imagen == "secundaria":
                        index_imagen_a_eliminar = producto["imagenes_productos"][index]
                        resultado = mongo.actualizar_imagenes_secundarias(id_producto, index_imagen_a_eliminar, "pull")

                        #* TODO: Eliminar del frontend mensaje de confirmacion "status_imagen_eliminada"
                        if resultado == "actualizada":
                            return jsonify({"status_imagen_eliminada": "correcto", "mensaje": "Imagen eliminada"}), 200
                        else:
                            return jsonify({"mensaje": "Error al eliminar imagen"}), 500  

            except Exception as e:
                print(e)
                return jsonify({"status_imagen_eliminada": "error"})
        else:
            return jsonify({"error": "no existe el id"})
        
 
    def crear_imagen(self):

        try:
            imagen_principal = request.files.getlist('imagen_principal')
            imagenes_secundarias = request.files.getlist('imagenes_secundarias')

            # Se sube imagen principal
            url_imagen_principal = cloudinary_bd.subir_imagen(imagen_principal[0])

            # Se suben las imagenes secundarias
            urls_imagenes_secundarias = []
            for imagen in imagenes_secundarias:
                url_imagen = cloudinary_bd.subir_imagen(imagen)
                urls_imagenes_secundarias.append(url_imagen)

            return jsonify({"urls_imagenes_secundarias": urls_imagenes_secundarias, "url_imagen_principal": url_imagen_principal})
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500    
         
    def insertar_producto(self):

        nuevo_producto = {
            "_id": request.json['_id'],
            "nombre_producto": request.json['nombre_producto'],
            "categoria": request.json['categoria'],
            "descripcion": request.json['descripcion'],
            "precio": int(request.json['precio']),
            "descuento": int(request.json['descuento']),
            "imagen_principal": request.json['imagen_principal'],
            "imagenes_productos": request.json['imagenes_productos'],
            "dimensiones": request.json['dimensiones'],
            "material": request.json['material']
        }
        
        resultado = mongo.insertar_producto(nuevo_producto)

        if resultado == "agregado":
            return jsonify({"mensaje": "Producto insertado correctamente"}), 200
        else:
            return jsonify({"mensaje": "error al insertar nuevo producto"}), 500       
        
    def guardar_imagen(self):
        
        try:
            imagenes = request.files.getlist('imagenes')
            # * Segun el tipo de imagen, se usa una funcion distinta en la bd
            tipo_imagen = request.form.get('tipo_imagen')
            id = request.form.get('id')

            # * Se puede guardar una imagen o varias y dependiendo del tipo de imagen
            # * se hace una operacion u otra (condiciones mas abajo)
            urls_imagenes = []

            # * Se sube una o varias imagenes
            for imagen in imagenes:
                url_imagen = cloudinary_bd.subir_imagen(imagen)
                urls_imagenes.append(url_imagen)

            # * Se envia solamente la url de la imagen sola
            if tipo_imagen == "imagen principal":
                resultado = mongo.actualizar_imagen_principal(id, urls_imagenes[0])
                if resultado == "actualizada":
                    return jsonify({"urls_imagenes": urls_imagenes,
                                    "mensaje": "imagen principal actualizada"}), 200
                else:
                    return jsonify({"mensaje": "error al actualizar imagen principal"}), 500
                
            # * Se envia las url de las imagenes
            if tipo_imagen == "imagenes secundarias":
                resultado = mongo.actualizar_imagenes_secundarias(id, urls_imagenes, "set")
                if resultado == "actualizada":
                    return jsonify({"urls_imagenes": urls_imagenes,
                                    "mensaje": "imagenes secundarias actualizadas"}), 200
                else:
                    return jsonify({"mensaje": "error al actualizar imagenes secundarias"}), 500
                
        except Exception as e:  
            return jsonify({"error": str(e)}), 500
     
    def get_productos(self):
        lista_productos = mongo.traer_productos()
        datos = []
        for producto in lista_productos:
            datos.append(producto)
        
        return jsonify({"productos": datos}), 200
     
    def editar_campo_producto(self):

        id = str(request.json['_id'])

        productos_editar = {
            "nombre_producto": request.json['nombre_producto'],
            "categoria": request.json['categoria'],
            "descripcion": request.json['descripcion'],
            "precio": int(request.json['precio']),
            "descuento": int(request.json['descuento']),
            "dimensiones": request.json['dimensiones'],
            "material": request.json['material']
        }

        resultado = mongo.actualizar_datos_productos(id, productos_editar)

        if resultado == "actualizada":
            return jsonify({"mensaje": "Producto actualizado correctamente"}), 200
        else:
            return jsonify({"mensaje": "error al actualizar informacion del producto"}), 500
        
    #TODO: En la web hay que enviarle el id del producto
    def eliminar_producto(self, id_producto):

        resultado = mongo.eliminar_producto(id_producto)

        if resultado == "eliminado":
            return jsonify({"mensaje": "Producto eliminado correctamente"})
        else:
            return jsonify({"mensaje": "No se encontró ningún producto con el ID especificado"})