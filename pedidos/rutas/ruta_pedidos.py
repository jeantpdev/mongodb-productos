from flask import Flask, jsonify, request, Blueprint
from flask_cors import cross_origin
from flasgger import swag_from
from pedidos.controladores.controlador_pedidos import *

con_pedidos = Controlador_Pedidos()

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/crear-pedido/', methods=['POST'])
@swag_from({
    'summary': 'Registrar un nuevo pedido',
    'description': 'Endpoint para registrar un nuevo pedido',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                    'datosCliente': {
                        'type': 'object',
                        'properties': {
                            'nombre': {'type': 'string', 'example': 'Juan'},
                            'apellido': {'type': 'string', 'example': 'Pérez'},
                            'correo': {'type': 'string', 'example': 'juan.perez@example.com'},
                            'numero': {'type': 'string', 'example': '123456789'},
                            'ciudad': {'type': 'string', 'example': 'Barranquilla'},
                            'direccion': {'type': 'string', 'example': 'Calle Falsa 123'}
                        },
                        'required': ['nombre', 'apellido', 'correo', 'numero', 'ciudad', 'direccion']
                    },
                    'pedido': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'producto': {'type': 'string', 'example': 'Nintendo Controller'},
                                'cantidad': {'type': 'integer', 'example': 2},
                                'precio': {'type': 'number', 'format': 'int', 'example': 120000}
                            },
                            'required': ['producto', 'cantidad', 'precio']
                        }
                    }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'El pedido se ha registrado en la BD',
            'examples': {
                'application/json': {
                    'msg': 'Pedido registrado exitosamente'
                }
            }
        },
        500: {
            'description': 'Error interno del servidor',
            'examples': {
                'application/json': {
                    'error': "error",
                    'mensaje': 'Error al registrar el pedido'
                }
            }
        }
    }
})
@cross_origin()
def post_pedido():
      return con_pedidos.post_pedido() 
      
@pedidos.route('/pedidos/', methods=['GET'])
@swag_from({
    'summary': 'Obtener la lista de pedidos',
    'description': 'Endpoint para obtener la lista de pedidos.',
    'responses': {
        200: {
            'description': 'Lista de pedidos obtenida exitosamente.',
            'schema': {
                'type': 'object',
                'properties': {
                    'pedidos': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'nombre_producto': {'type': 'string'},
                                '_id': {'type': 'string'},
                                'nombre': {'type': 'string'},
                                'apellido': {'type': 'string'},
                                'numero': {'type': 'string'},
                                'ciudad': {'type': 'string'},
                                'direccion': {'type': 'string'},
                                'correo': {'type': 'string'},
                                'pedido': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'nombre_producto': {'type': 'string'},
                                            'material': {'type': 'string'},
                                            'cantidad': {'type': 'integer'},
                                            'descuento': {'type': 'number'},
                                            'total': {'type': 'number'},
                                            'precio_total': {'type': 'number'}
                                        }
                                    }
                                },
                                'fecha': {'type': 'string', 'format': 'date'},
                                'hora': {'type': 'string', 'format': 'time'}
                            }
                        }
                    }
                }
            }
        }
    }
})
@cross_origin()
def get_pedidos():
      return con_pedidos.get_pedidos()

