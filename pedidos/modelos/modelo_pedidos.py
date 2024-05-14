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
            
            # Crear una lista de productos formateados
            productos_formateados = []
            for producto in pedido['pedido']:
                producto_formateado = {
                    "nombre_producto": producto['nombre_producto'],
                    "material": producto['material'],
                    "cantidad": producto['cantidad'],
                    "descuento": producto['descuento'],
                    "total": producto['total'],
                    "precio_total": producto['precio_total']
                }
                productos_formateados.append(producto_formateado)

            # Crear un nuevo diccionario con los campos modificados
            pedido_formateado = {
                "_id": str(pedido['_id']),
                "nombre": pedido['nombre'],
                "apellido": pedido['apellido'],
                "numero": pedido['numero'],
                "ciudad": pedido['ciudad'],
                "direccion": pedido['direccion'],
                "pedido": productos_formateados,
                "fecha": fecha_formateada,
                "hora": hora_formateada,
                "imagen_producto": pedido['imagen_producto']
            }
            
            datos.append(pedido_formateado)
        
        return jsonify({"pedidos": datos}), 200

