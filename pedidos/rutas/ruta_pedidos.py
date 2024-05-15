from flask import Flask, jsonify, request, Blueprint
from flask_cors import cross_origin
from pedidos.controladores.controlador_pedidos import *

con_pedidos = Controlador_Pedidos()

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/crear-pedido/', methods=['POST'])
@cross_origin()
def post_pedido():
      return con_pedidos.post_pedido() 
      
@pedidos.route('/pedidos/', methods=['GET'])
@cross_origin()
def get_pedidos():
      return con_pedidos.get_pedidos()

