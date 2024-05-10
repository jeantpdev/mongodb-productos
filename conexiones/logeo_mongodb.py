from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

class mongo:

    #TODO: Agregarle las excepciones a todas las funciones

    def conexion_mongodb_logeo():
        client = MongoClient(os.getenv('MONGO_URI_LOGEO'))
        db = client.Users
        return db

    def buscar_dato(nombre_columna, dato):
        db_logeo = mongo.conexion_mongodb_logeo()
        dato = db_logeo.usuarios.find_one({nombre_columna: dato})
        return dato
    
    def crear_usuario(email, username, rol, password):
        db_logeo = mongo.conexion_mongodb_logeo()
        try:
            user_id = db_logeo.usuarios.insert_one({'email': email,'username': username, 'rol': rol, 'password': password})
            return user_id.inserted_id
            
        except Exception as e:
            return "error" + e
    

