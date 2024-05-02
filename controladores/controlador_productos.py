from modelos.modelo_productos import *

mod_formulario = Formulario()

class Formulario_Controlador():
    
    def get_productos(self):
        query = mod_formulario.get_productos()
        return query
    
    def post_producto(self):
        query = mod_formulario.insertar_producto()
        return query
    
    def update_campo_producto(self, id_producto):
        query = mod_formulario.editar_campo_producto(id_producto)
        return query
    
    def delete_producto(self, id_producto):
        query = mod_formulario.eliminar_producto(id_producto)
        return query