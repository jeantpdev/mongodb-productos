from flask import Flask, jsonify, request, Blueprint
from flask_cors import cross_origin
from logeo.controladores.controlador_logeo import *

con_logeo = Controlador_Logeo()

logeo = Blueprint('logeo', __name__)

@logeo.route('/iniciar-sesion/', methods=['POST'])
@cross_origin()
def login():
      return con_logeo.post_iniciar_sesion()

@logeo.route('/registro/', methods=['POST'])
@cross_origin()
def registro():
      return con_logeo.post_registro()
