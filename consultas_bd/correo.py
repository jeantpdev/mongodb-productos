from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from conexiones.conexionCorreo import *

class Correo:
    @staticmethod
    def crear_mensaje(datos):
        mail_from = os.getenv('CORREO')
        mail_to = os.getenv('CORREO')  # Cambié esto para enviar el correo al destinatario proporcionado

        # Asunto y cuerpo del correo
        mail_subject = "Ha llegado un pedido nuevo"
        mail_body = f"¡Hola! Se ha recibido un nuevo pedido.\n\n"
        
        mail_body += f"Nombre: {datos['nombre']} {datos['apellido']}\n"
        mail_body += f"Correo electrónico: {datos['correo']}\n"
        mail_body += f"Número de contacto: {datos['numero']}\n"
        mail_body += f"Ciudad: {datos['ciudad']}\n"
        mail_body += f"Dirección: {datos['direccion']}\n"
        mail_body += f"Fecha del pedido: {datos['fecha'].strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        mail_body += "Detalles del pedido:\n"
        for i, producto in enumerate(datos['pedido'], start=1):
            mail_body += f"Producto {i}:\n"
            mail_body += f"  Nombre: {producto['nombre_producto']}\n"
            mail_body += f"  Material: {producto['material']}\n"
            mail_body += f"  Descuento: {producto['descuento']}%\n"
            mail_body += f"  Cantidad: {producto['cantidad']}\n"
            mail_body += f"  Precio total: {producto['precio_total']}\n\n"
        
        mail_body += "Enviado automáticamente desde Python\n"

        mimemsg = MIMEMultipart()
        mimemsg['From'] = mail_from
        mimemsg['To'] = mail_to
        mimemsg['Subject'] = mail_subject
        mimemsg.attach(MIMEText(mail_body, 'plain'))
        
        return mimemsg

    @staticmethod
    def enviar_correo(datos):
        connection = Conexion_correo.conectar_correo()
        mensaje = Correo.crear_mensaje(datos)
        try:
            connection.send_message(mensaje)
            print("Correo enviado correctamente.")
        except Exception as e:
            print(f"Error al enviar el correo: {str(e)}")
        finally:
            connection.quit()