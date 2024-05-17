from librerias import *
from productos.controladores.controlador_productos import *
from flasgger import swag_from

con_formulario = Formulario_Controlador()

#TODO: Validación | Mejorar mensajes de respuestas
#TODO: Validación | Rutas protegidas por Token

productos = Blueprint('productos', __name__)

def autenticar_usuario(datos_usuario):
   rol_usuario = datos_usuario['user_rol']
   if rol_usuario != 'admin':
      acceso = False
   else:
      acceso = True
   return acceso
   
@productos.route('/eliminar-imagen/', methods=['POST'])
@swag_from({
    'summary': 'Eliminar imagen',
    'description': 'Endpoint para eliminar una imagen existente de Cloudinary',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'example': '2'},
                    'imagen_url': {'type': 'string', 'example': 'urlcloudinary.com'},
                    'tipo_imagen': {'type': 'string', 'example': 'contrasena123'},
                    'index': {'type': 'int', 'example': '2'}

                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Se pudo eliminar la imagen',
            'examples': {
                'application/json': {
                    'status_imagen_eliminada': 'correcto',
                    'mensaje': 'Imagen eliminada'
                },
                'application/json': {
                    'status_imagen_eliminada': 'correcto',
                    'mensaje': 'Imagen eliminada'
                }
            }
        },
        500: {
            'description': 'No se pudo eliminar la imagen',
            'examples': {
                'application/json': {
                    'mensaje': 'Error al eliminar la imagen'
                },
                'application/json': {
                    "status_imagen_eliminada": "error"
                }
            }
        },
        403: {
            'description': 'No contiene un token de acceso',
            'examples': {
                'application/json': {
                  'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'
                }
            }
        }
    }
})
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

@productos.route('/crear-imagen/', methods=['POST'])
@swag_from({
    'summary': 'Subir imagen a cloudinary',
    'description': 'Endpoint para subir una imagen a Cloudinary',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'formdata',
                'properties': {
                    'imagen_principal': {'type': 'file', 'example': 'imagenFormData'},
                    'imagenes_secundarisa': {'type': 'file', 'example': 'imagenFormData'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Creacion de imagen exitosa',
            'examples': {
                'application/json': {
                    'urls_imagenes_secundarias': 'https://cloudinary.com/url_cloudinary',
                    'url_imagen_principal': 'https://cloudinary.com/url_cloudinary'
                }
            }
        },
        500: {
            'description': 'No se pudo subir las imagenes',
            'examples': {
                'application/json': {
                    'mensaje': 'error'
                }
            }
        },
        403: {
            'description': 'No contiene un token de acceso',
            'examples': {
                'application/json': {
                  'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'
                }
            }
        }
    }
})
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

@productos.route('/guardar-imagen/', methods=['POST'])
@swag_from({
    'summary': 'Permite actualizar la imagen principal o la secundaria',
    'description': 'Endpoint para actualizar la imagen principal o la secundaria',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'imagenes': {'type': 'file', 'example': 'imagenFormData'},
                    'tipo_imagen': {'type': 'string', 'example': 'imagen_principal'},
                    'id': {'type': 'string', 'example': '2'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Se actualiza la imagen principal o las secundarias',
            'examples': {
                'application/json': {
                    'urls_imagenes': 'https://cloudinary.com/url_cloudinary',
                    'mensaje': 'imagen principal actualizada'
                },
                 'application/json': {
                    'urls_imagenes': 'https://cloudinary.com/url_cloudinary',
                    'mensaje': 'imagenes secundarias actualizadas'
                }
            }
        },
        500: {
            'description': 'No se pudo subir las imagenes',
            'examples': {
                'application/json': {
                    'mensaje': 'error al actualizar imagenes secundarias'
                },
                'application/json': {
                    'mensaje': 'error'
                }
            }
        },
        403: {
            'description': 'No contiene un token de acceso',
            'examples': {
                'application/json': {
                  'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'
                }
            }
        }
    }
})
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
   
@productos.route('/productos/', methods=['GET'])
@swag_from({
    'summary': 'Eliminar imagen',
    'description': 'Endpoint para eliminar una imagen existente de Cloudinary',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                        "_id": {'type': 'string', 'example': '2'},
                        "nombre_producto": {'type': 'string', 'example': 'Nintendo Controller'},
                        "categoria": {'type': 'string', 'example': 'Tecnologia'},
                        "descripcion": {'type': 'string', 'example': 'Control para juegos'},
                        "precio": {'type': 'int', 'example': '25000'},
                        "descuento": {'type': 'int', 'example': '20'},
                        "imagen_principal": {'type': 'string', 'example': 'url-imagen'},
                        "imagenes_productos": {'type': 'array', 'example': ['url-imagen', 'url-imagen', 'url-imagen']},
                        "dimensiones": {'type': 'string', 'example': '20cmx20cm'},
                        "material": {'type': 'string', 'example': 'Cuero'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Se pudo eliminar la imagen',
            'examples': {
                'application/json': {
                        "_id": "66247",
                        "nombre_producto": "SHARON MINA WALLPAPER",
                        "categoria": "Wallpapers",
                        "descripcion": "Wallpaper gigante de Mina Sharon",
                        "precio": 250000,
                        "descuento": 12,
                        "imagen_principal": "https://res.cloudinary.com/duxf5m5c2/image/upload/v1715143722/w8qekffzcsvxszoavzqi.jpg",
                        "imagenes_productos": [
                           "https://res.cloudinary.com/duxf5m5c2/image/upload/v1715143722/hnm1cb0myjzjeks3c83k.jpg",
                           "https://res.cloudinary.com/duxf5m5c2/image/upload/v1715143723/zjaijc1qtiy6dwt9dbae.jpg"
                        ],
                        "dimensiones": "50cmx50cm",
                        "material": "papel"
                }
            }
        }
    }
})
@cross_origin()
def get_productos():
      return con_formulario.get_productos()
    
@productos.route('/insertar-producto/', methods=['POST'])
@swag_from({
    'summary': 'Insertar nuevo producto',
    'description': 'Endpoint para insertar un nuevo producto',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                        "_id": {'type': 'string', 'example': '2'},
                        "nombre_producto": {'type': 'string', 'example': 'Nintendo Controller'},
                        "categoria": {'type': 'string', 'example': 'Tecnologia'},
                        "descripcion": {'type': 'string', 'example': 'Control para juegos'},
                        "precio": {'type': 'int', 'example': '25000'},
                        "descuento": {'type': 'int', 'example': '20'},
                        "imagen_principal": {'type': 'string', 'example': 'url-imagen'},
                        "imagenes_productos": {'type': 'array', 'example': ['url-imagen', 'url-imagen', 'url-imagen']},
                        "dimensiones": {'type': 'string', 'example': '20cmx20cm'},
                        "material": {'type': 'string', 'example': 'Cuero'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Producto insertado en la base de datos',
            'examples': {
                'application/json': {
                  "mensaje": "Producto insertado correctamente"
                }
            }
        },
        500: {
            'description': 'No se pudo insertar el producto',
            'examples': {
                'application/json': {
                  "mensaje": "Error al insertar nuevo productp"
                }
            }
        },
        403: {
            'description': 'No contiene un token de acceso',
            'examples': {
                'application/json': {
                  'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'
                }
            }
        }
    }
})
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

@productos.route('/editar-producto/', methods=['PUT'])
@swag_from({
    'summary': 'Editar un producto',
    'description': 'Endpoint para editar los datos de un producto sin contar las imagenes',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                        "_id": {'type': 'string', 'example': '2'},
                        "nombre_producto": {'type': 'string', 'example': 'Nintendo Controller'},
                        "categoria": {'type': 'string', 'example': 'Tecnologia'},
                        "descripcion": {'type': 'string', 'example': 'Control para juegos'},
                        "precio": {'type': 'int', 'example': '25000'},
                        "descuento": {'type': 'int', 'example': '20'},
                        "dimensiones": {'type': 'string', 'example': '20cmx20cm'},
                        "material": {'type': 'string', 'example': 'Cuero'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Producto editado',
            'examples': {
                'application/json': {
                  "mensaje": "Producto actualizado correctamente"
                }
            }
        },
        500: {
            'description': 'No se pudo editar el producto',
            'examples': {
                'application/json': {
                  "mensaje": "error al actualizar informacion del producto"
                }
            }
        },
        403: {
            'description': 'No contiene un token de acceso',
            'examples': {
                'application/json': {
                  'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'
                }
            }
        }
    }
})
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

@productos.route('/eliminar-producto/<id_producto>', methods=['DELETE'])
@swag_from({
    'summary': 'Insertar nuevo producto',
    'description': 'Endpoint para insertar un nuevo producto',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                        "_id": {'type': 'string', 'example': '2'},
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Producto eliminad de la base de datos',
            'examples': {
                'application/json': {
                  "mensaje": "Producto eliminado correctamente"
                }
            }
        },
        500: {
            'description': 'No se pudo eliminar el producto',
            'examples': {
                'application/json': {
                  "mensaje": "No se encontró ningún producto con el ID especificado"
                }
            }
        },
        403: {
            'description': 'No contiene un token de acceso',
            'examples': {
                'application/json': {
                  'mensaje': 'Acceso denegado! Solo los administradores pueden acceder a esta ruta.'
                }
            }
        }
    }
})
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