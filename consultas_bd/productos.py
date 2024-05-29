from conexiones.conexionMongoDB import *

class consultas_productos:

    #TODO: Agregar busqueda de una columna en especifico

    def buscar_producto(id):
        db = mongo.coleccion_productos()
        producto = db.lista_productos.find_one({"_id": id})
        return producto
    
    def eliminar_producto(id):
        db = mongo.coleccion_productos()
        resultado = db.lista_productos.delete_one({"_id": str(id)})
        if resultado.deleted_count == 1:
            return "eliminado"  # Producto eliminado correctamente
        else:
            return "no eliminado"  # No se pudo eliminar el producto
    
    def insertar_producto(nuevo_producto):
        db = mongo.coleccion_productos()
        resultado = db.lista_productos.insert_one(nuevo_producto)

        if resultado.inserted_id:
            return "agregado"
        else:
            return "no agregado"
    
    def traer_productos():
        db = mongo.coleccion_productos()
        lista_productos = db.lista_productos.find()
        return lista_productos

    def actualizar_datos_productos(id, info_productos_editar):
        db = mongo.coleccion_productos()
        resultado = db.lista_productos.update_many(
            {"_id": id},
            {"$set": info_productos_editar})
        
        if resultado.modified_count == 1:
            return "actualizada"
        else:
            return "no actualizada"
        
    def actualizar_imagen_principal(id, imagen):
        db = mongo.coleccion_productos()
        resultado = db.lista_productos.update_one(
        {"_id": id},
        {"$set": {"imagen_principal": imagen}})

        if resultado.modified_count == 1:
            return "actualizada"
        else:
            return "no actualizada"
        
    def actualizar_imagenes_secundarias(id, imagen, tipo):
        db = mongo.coleccion_productos()
        # * Agrega varias imagenes
        print(tipo)
        if(tipo == "set"):
            resultado = db.lista_productos.update_one(
                {"_id": id},
                {"$addToSet": {"imagenes_productos": {"$each": imagen}}})

            if resultado.modified_count == 1:
                return "actualizada"
            else:
                return "no actualizada"
            
        # * Elimina una imagen en especifico
        if (tipo == "pull"):
            resultado = db.lista_productos.update_one(
                {"_id": id},
                {"$pull": {"imagenes_productos": imagen}})
            
            if resultado.modified_count == 1:
                return "actualizada"
            else:
                return "no actualizada"