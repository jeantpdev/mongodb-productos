from librerias import *
from controladores.controlador_productos import *

con_formulario = Formulario_Controlador()

#TODO: Validación | Mejorar mensajes de respuestas
#TODO: Validación | Rutas protegidas por Token

todo = Blueprint('todo', __name__)

def autenticar_usuario(datos_usuario):
   rol_usuario = datos_usuario['user_rol']
   if rol_usuario != 'admin':
      acceso = False
   else:
      acceso = True
   return acceso
   
@todo.route('/eliminar-imagen/', methods=['POST'])
@cross_origin()
@jwt_required()
def delete_imagen_productos():
   try:
      identidad = get_jwt_identity()
      acceso = autenticar_usuario(identidad)
      if acceso == False:
         return jsonify({'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'}), 403
      if acceso == True:
         return con_formulario.delete_imagen()
      
   except Exception as e:
          return jsonify({"error": str(e)}), 500     


@todo.route('/crear-imagen/', methods=['POST'])
@cross_origin()
@jwt_required()
def post_crear_imagen_producto():
   try:
      identidad = get_jwt_identity()
      acceso = autenticar_usuario(identidad)
      if acceso == False:
         return jsonify({'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'}), 403
      if acceso == True:
          return con_formulario.post_crear_imagen()
   except Exception as e:
          return jsonify({"error": str(e)}), 500     

@todo.route('/guardar-imagen/', methods=['POST'])
@cross_origin()
@jwt_required()
def post_imagen_productos():
   try:
      identidad = get_jwt_identity()
      acceso = autenticar_usuario(identidad)
      if acceso == False:
         return jsonify({'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'}), 403
      if acceso == True:
         return con_formulario.post_imagen()
      
   except Exception as e:
          return jsonify({"error": str(e)}), 500     
   
@todo.route('/productos/', methods=['GET'])
@cross_origin()
def get_productos():
      return con_formulario.get_productos()
    
@todo.route('/insertar-producto/', methods=['POST'])
@cross_origin()
@jwt_required()
def post_producto():
   try:
      identidad = get_jwt_identity()
      acceso = autenticar_usuario(identidad)
      if acceso == False:
         return jsonify({'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'}), 403
      if acceso == True:
         return con_formulario.post_producto()
         
   except Exception as e:
          return jsonify({"error": str(e)}), 500     

@todo.route('/editar-producto/', methods=['PUT'])
@cross_origin()
@jwt_required()
def update_campo_producto():
   try:
      identidad = get_jwt_identity()
      acceso = autenticar_usuario(identidad)
      if acceso == False:
         return jsonify({'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'}), 403
      if acceso == True:
         return con_formulario.update_campo_producto()

   except Exception as e:
          return jsonify({"error": str(e)}), 500     

@todo.route('/eliminar-producto/<id_producto>', methods=['DELETE'])
@cross_origin()
@jwt_required()
def delete_producto(id_producto):
   try:
      identidad = get_jwt_identity()
      acceso = autenticar_usuario(identidad)
      if acceso == False:
         return jsonify({'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'}), 403
      if acceso == True:
         return con_formulario.delete_producto(id_producto)

   except Exception as e:
          return jsonify({"error": str(e)}), 500     