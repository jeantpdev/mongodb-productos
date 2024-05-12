from conexiones.conexionMongoDB import *

class consultas_pedidos:

    def traer_pedidos():
        db = mongo.coleccion_pedidos()
        lista_pedidos = db.lista_pedidos.find()
        return lista_pedidos
