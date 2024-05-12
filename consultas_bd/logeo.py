from conexiones.conexionMongoDB import *

class consultas_logeo:

    #TODO: Agregarle las excepciones a todas las funciones
    def buscar_dato(nombre_columna, dato):
        db_users = mongo.coleccion_usuarios()
        dato = db_users.usuarios.find_one({nombre_columna: dato})
        return dato
    
    def crear_usuario(email, username, rol, password):
        db_users = mongo.coleccion_usuarios()
        try:
            user_id = db_users.usuarios.insert_one({'email': email,'username': username, 'rol': rol, 'password': password})
            return user_id.inserted_id
            
        except Exception as e:
            return "error" + e
    

