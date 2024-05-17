from consultas_bd.logeo import *
from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token
from datetime import datetime, timedelta
import bcrypt

#TODO: NO ESTA AGREGADO LOADENV
class Modelo_Logeo():

    def iniciar_sesion(self):
        
        email = request.json.get('email')
        password = request.json.get('password')

        user = consultas_logeo.buscar_dato("email", email)

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            user_rol = user['rol']
            expiry_time = timedelta(hours = 24)
            access_token = create_access_token(identity={"user_rol": user_rol, "mensaje": "hola"}, expires_delta = expiry_time)# En la función login()
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"msg": "Credenciales inválidas"}), 401
        
    def registro(self):

        data = request.get_json()
        username = data.get('username', None)
        email = data.get('email', None)
        password = data.get('password', None)
        rol = data.get('rol', None)
        
        if consultas_logeo.buscar_dato("email", email):
            return jsonify({"msg": "El correo ya está en uso"}), 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        res = consultas_logeo.crear_usuario(email, username, rol, hashed_password)

        if (res):
            return jsonify({"msg": "Usuario registrado exitosamente", "user_id": str(res)}), 201
        else:  
            return jsonify({"msg": res}), 5000