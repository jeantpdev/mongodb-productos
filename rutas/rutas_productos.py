from librerias import *
from controladores.controlador_productos import *

con_formulario = Formulario_Controlador()

todo = Blueprint('todo', __name__)

@todo.route('/productos/', methods=['GET'])
@cross_origin()  
def get_productos():
   return con_formulario.get_productos()

@todo.route('/insertar-producto/', methods=['POST'])
@cross_origin()  
def post_producto():
   return con_formulario.post_producto()

@todo.route('/editar-producto/', methods=['PUT'])
@cross_origin()  
def update_campo_producto():
   return con_formulario.update_campo_producto()


@todo.route('/eliminar-producto/<id_producto>', methods=['DELETE'])
@cross_origin()  
def delete_producto(id_producto):
   return con_formulario.delete_producto(id_producto)