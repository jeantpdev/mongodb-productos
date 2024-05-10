from logeo.modelos.modelo_logeo import *

mod_logeo = Modelo_Logeo()

class Controlador_Logeo():

    def post_iniciar_sesion(self):
        query = mod_logeo.iniciar_sesion()
        return query
    
    def post_registro(self):
        query = mod_logeo.registro()
        return query