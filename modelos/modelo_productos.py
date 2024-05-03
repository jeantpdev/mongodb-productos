from librerias import *

class Formulario():

    def get_productos(self):
        client = MongoClient('mongodb+srv://jeantpdev:2HH3bRjoUMrUMGYU@productos.ns6gatt.mongodb.net/')
        db = client.Productos
        
        lista_productos = db.lista_productos.find()
        datos = []

        for producto in lista_productos:
            datos.append(producto)
        
        return jsonify({"productos": datos})
    
    def insertar_producto(self):

        client = MongoClient('mongodb+srv://jeantpdev:2HH3bRjoUMrUMGYU@productos.ns6gatt.mongodb.net/')
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
    
    def editar_campo_producto(self):

        client = MongoClient('mongodb+srv://jeantpdev:2HH3bRjoUMrUMGYU@productos.ns6gatt.mongodb.net/')
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
            {"$set": info_producto_editar}
        )

        return jsonify({"mensaje": "Producto actualizado correctamente"})
    
    def eliminar_producto(self, id_producto):
        client = MongoClient('mongodb+srv://jeantpdev:2HH3bRjoUMrUMGYU@productos.ns6gatt.mongodb.net/')
        db = client.Productos

        id = str(id_producto)

        resultado = db.lista_productos.delete_one({"_id": id})

        # Verificar si se eliminó el documento
        if resultado.deleted_count == 1:
            return jsonify({"mensaje": "Producto eliminado correctamente"})
        else:
            return jsonify({"mensaje": "No se encontró ningún producto con el ID especificado"})