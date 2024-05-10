from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

class mongo:

    #TODO: Agregar busqueda de una columna en especifico

    def conexion_mongo():
        client = MongoClient(os.getenv('MONGO_URI'))
        db = client.Productos
        return db

    def buscar_producto(id):
        db = mongo.conexion_mongo()
        producto = db.lista_productos.find_one({"_id": id})
        return producto
    
    def insertar_producto(nuevo_producto):
        db = mongo.conexion_mongo()
        resultado = db.lista_productos.insert_one(nuevo_producto)

        if resultado.inserted_id:
            return "agregado"
        else:
            return "no agregado"
    
    def traer_productos():
        db = mongo.conexion_mongo()
        lista_productos = db.lista_productos.find()
        return lista_productos

    def actualizar_datos_productos(id, info_productos_editar):
        db = mongo.conexion_mongo()

        resultado = db.lista_productos.update_many(
            {"_id": id},
            {"$set": info_productos_editar})
        
        if resultado.modified_count > 0:
            return "actualizada"
        else:
            return "no actualizada"
        
    def actualizar_imagen_principal(id, imagen):
        db = mongo.conexion_mongo()
        resultado = db.lista_productos.update_one(
        {"_id": id},
        {"$set": {"imagen_principal": imagen}})

        if resultado.modified_count > 0:
            return "actualizada"
        else:
            return "no actualizada"
        
    def actualizar_imagenes_secundarias(id, imagen, tipo):
        db = mongo.conexion_mongo()
        # * Agrega varias imagenes
        print(tipo)
        if(tipo == "set"):
            resultado = db.lista_productos.update_one(
                {"_id": id},
                {"$addToSet": {"imagenes_productos": {"$each": imagen}}})
            print(resultado)
            if resultado.modified_count > 0:
                return "actualizada"
            else:
                return "no actualizada"
            
        # * Elimina una imagen en especifico
        if (tipo == "pull"):
            print("entraste en la funcion pull")
            resultado = db.lista_productos.update_one(
                {"_id": id},
                {"$pull": {"imagenes_productos": imagen}})
            
            if resultado.modified_count > 0:
                return "actualizada"
            else:
                return "no actualizada"