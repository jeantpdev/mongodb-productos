from conexiones.conexionMongoDB import *

class consultas_pedidos:

    def traer_pedidos():
        db = mongo.coleccion_pedidos()
        lista_pedidos = db.lista_pedidos.find()
        return lista_pedidos
    

    def crear_pedido(pedido):
        db = mongo.coleccion_pedidos()
        resultado = db.lista_pedidos.insert_one(pedido)
        print(resultado)

        if resultado.inserted_id:
            return "agregado"
        else:
            return "no agregado"
