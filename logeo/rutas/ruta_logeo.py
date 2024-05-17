from flask import Flask, jsonify, request, Blueprint
from flask_cors import cross_origin
from flasgger import swag_from
from logeo.controladores.controlador_logeo import *

con_logeo = Controlador_Logeo()

logeo = Blueprint('logeo', __name__)

@logeo.route('/iniciar-sesion/', methods=['POST'])
@swag_from({
    'summary': 'Iniciar sesión',
    'description': 'Endpoint para iniciar sesión',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string', 'example': 'usuario@ejemplo.com'},
                    'password': {'type': 'string', 'example': 'contrasena123'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Inicio de sesión exitoso',
            'examples': {
                'application/json': {
                    'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
                }
            }
        },
        401: {
            'description': 'Credenciales inválidas',
            'examples': {
                'application/json': {
                    'msg': 'Credenciales inválidas'
                }
            }
        }
    }
})
@cross_origin()
def login():
      return con_logeo.post_iniciar_sesion()

@logeo.route('/registro/', methods=['POST'])
@swag_from({
    'summary': 'Registro de usuario',
    'description': 'Endpoint para registrar un nuevo usuario',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string', 'example': 'juanperez'},
                    'email': {'type': 'string', 'example': 'juan.perez@example.com'},
                    'password': {'type': 'string', 'example': 'contrasena123'},
                    'rol': {'type': 'string', 'example': 'admin'}
                },
                'required': ['username', 'email', 'password', 'rol']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Usuario registrado exitosamente',
            'examples': {
                'application/json': {
                    'msg': 'Usuario registrado exitosamente',
                    'user_id': '1234567890'
                }
            }
        },
        400: {
            'description': 'El correo ya está en uso',
            'examples': {
                'application/json': {
                    'msg': 'El correo ya está en uso'
                }
            }
        },
        500: {
            'description': 'Error interno del servidor',
            'examples': {
                'application/json': {
                    'msg': 'Error al registrar el usuario'
                }
            }
        }
    }
})
@cross_origin()
def registro():
      return con_logeo.post_registro()
