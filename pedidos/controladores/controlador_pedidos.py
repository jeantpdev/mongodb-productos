from pedidos.modelos.modelo_pedidos import *

mod_pedidos = Modelo_Pedidos()

class Controlador_Pedidos:

    def get_pedidos(self):
        query = mod_pedidos.traer_pedidos()
        return query
    
    def post_pedido(self):
        query = mod_pedidos.crear_pedido()
        return query