from consultas_bd.pedidos import *
from consultas_bd.correo import *
from flask import Flask, request, jsonify
from datetime import datetime

class Modelo_Pedidos():

    def traer_pedidos(self):
        lista_pedidos = consultas_pedidos.traer_pedidos()
        datos = []

        for pedido in lista_pedidos:
            # Convertir la fecha y hora al formato deseado
            fecha_formateada = pedido['fecha'].strftime("%d/%m/%Y")
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
                "nombre_producto": producto['nombre_producto'],
                "_id": str(pedido['_id']),
                "nombre": pedido['nombre'],
                "apellido": pedido['apellido'],
                "numero": pedido['numero'],
                "ciudad": pedido['ciudad'],
                "direccion": pedido['direccion'],
                "correo": pedido['correo'],
                "pedido": productos_formateados,
                "fecha": fecha_formateada,
                "hora": hora_formateada
            }
            
            datos.append(pedido_formateado)
        
        return jsonify({"pedidos": datos}), 200

    def crear_pedido(self):
        try:
            datos_cliente = request.json['datosCliente']
            datos_pedido = request.json['pedido']
            
            nuevo_pedido = {
                "nombre": datos_cliente['nombre'],
                "apellido": datos_cliente['apellido'],
                "correo": datos_cliente['correo'],
                "numero": datos_cliente['numero'],
                "ciudad": datos_cliente['ciudad'],
                "direccion": datos_cliente['direccion'],
                "fecha": datetime.utcnow(),  # Generar la fecha en el mismo formato
                "pedido": datos_pedido
            }

            Correo.enviar_correo(nuevo_pedido)

            #res = consultas_pedidos.crear_pedido(nuevo_pedido)
            
            #print(res)
            
            return jsonify({"pedido": "pedido"}), 200    

        except Exception as e:
            return jsonify({"error": str(e)}), 500    
    

