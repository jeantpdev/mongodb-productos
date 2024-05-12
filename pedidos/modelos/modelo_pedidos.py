from consultas_bd.pedidos import *
from flask import Flask, request, jsonify
from datetime import datetime

class Modelo_Pedidos():

    def traer_pedidos(self):
        lista_pedidos = consultas_pedidos.traer_pedidos()
        datos = []

        for pedido in lista_pedidos:
            # Convertir la fecha y hora al formato deseado
            fecha_formateada = pedido['fecha'].strftime("%m/%d/%Y")
            hora_formateada = pedido['fecha'].strftime("%H:%M:%S")
            
            # Crear un nuevo diccionario con los campos modificados
            pedido_formateado = {
                "_id": str(pedido['_id']),
                "nombre": pedido['nombre'],
                "apellido": pedido['apellido'],
                "numero": pedido['numero'],
                "ciudad": pedido['ciudad'],
                "direccion": pedido['direccion'],
                "pedido": ['pedido'],
                "fecha": fecha_formateada,
                "hora": hora_formateada,
                "nombre_producto": pedido['pedido']['nombre_producto']
            }
            
            datos.append(pedido_formateado)
        
        return jsonify({"pedidos": datos}), 200

