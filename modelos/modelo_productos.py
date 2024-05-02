from librerias import *

class Formulario():

    def get_productos(self):
        # Conexión a la instancia de MongoDB en localhost
        client = MongoClient('mongodb://localhost:27017/')
        db = client.Productos
        
        # Recuperar todos los documentos de la colección 'products'
        lista_productos = db.lista_productos.find()
        
        # Crear una lista para almacenar los datos recuperados
        datos = []
        
        # Iterar sobre los documentos y agregarlos a la lista
        for producto in lista_productos:
            datos.append(producto)
        
        # Imprimir o devolver los datos como JSON
        return jsonify({"productos": datos})
    
    def insertar_producto(self):
        # Conexión a la instancia de MongoDB en localhost
        client = MongoClient('mongodb://localhost:27017/')
        db = client.Productos
        id = request.json['_id']
        nombre = request.json['nombre_producto']
        categoria = request.json['categoria']
        descripcion = request.json['descripcion']
        precio = request.json['precio']
        descuento = request.json['descuento']
        imagen_principal = request.json['imagen_principal']
        imagenes_productos = request.json['imagenes_productos']
        dimensiones = request.json['dimensiones']
        material = request.json['material']

        # Crear el documento a insertar en la colección
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
        
        # Insertar el documento en la colección
        db.lista_productos.insert_one(documento)
        
        return jsonify({"mensaje": "Producto insertado correctamente"})
    
    def editar_campo_producto(self, id_producto):
        # Conexión a la instancia de MongoDB en localhost
        client = MongoClient('mongodb://localhost:27017/')
        db = client.Productos
        id = str(id_producto)
        imagenes_productos = request.json['imagenes_productos']

        print(id)
        print(imagenes_productos)

        # Actualizar el campo imagen_principal del documento con el _id especificado
        db.lista_productos.update_one(
            {"_id": id},
            {"$set": {"imagenes_productos": imagenes_productos}}
        )

        return jsonify({"mensaje": "Imagenes de productos actualizada correctamente"})
    
    def editar_campo_producto(self, id_producto):
        # Conexión a la instancia de MongoDB en localhost
        client = MongoClient('mongodb://localhost:27017/')
        db = client.Productos
        id = str(id_producto)
        imagenes_productos = request.json['imagenes_productos']

        # Actualizar el campo imagen_principal del documento con el _id especificado
        db.lista_productos.update_one(
            {"_id": id},
            {"$set": {"imagenes_productos": imagenes_productos}}
        )

        return jsonify({"mensaje": "Imagenes de productos actualizada correctamente"})
    
    def eliminar_producto(self, id_producto):
        # Conexión a la instancia de MongoDB en localhost
        client = MongoClient('mongodb://localhost:27017/')
        db = client.Productos
        id = str(id_producto)
        # Eliminar el documento con el _id especificado
        resultado = db.lista_productos.delete_one({"_id": id})

        # Verificar si se eliminó el documento
        if resultado.deleted_count == 1:
            return jsonify({"mensaje": "Producto eliminado correctamente"})
        else:
            return jsonify({"mensaje": "No se encontró ningún producto con el ID especificado"})