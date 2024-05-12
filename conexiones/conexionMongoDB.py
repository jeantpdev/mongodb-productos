from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

class mongo:

    #TODO: Agregar busqueda de una columna en especifico

    def conexion_mongo():
        client = MongoClient(os.getenv('MONGO_URI'))
        return client
    
    def coleccion_productos():
        client = mongo.conexion_mongo()
        db = client.Productos
        return db
    
    def coleccion_pedidos():
        client = mongo.conexion_mongo()
        db = client.Pedidos
        return db

    def coleccion_usuarios():
        client = mongo.conexion_mongo()
        db = client.Users
        return db
