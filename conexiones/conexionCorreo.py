import smtplib
import os

class Conexion_correo:

    @staticmethod
    def conectar_correo():
        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        # Asegúrate de usar la contraseña de aplicación generada en Gmail
        connection.login(os.getenv('CORREO'), os.getenv('PASS_CORREO'))
        return connection
