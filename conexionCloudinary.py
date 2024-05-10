import cloudinary
# Lectura de variables de entorno
from dotenv import load_dotenv
load_dotenv()
import os

class cloudinary_bd:

    def config_cloudinary():
        config = cloudinary.config( 
            cloud_name = os.getenv('CLOUD_NAME'), 
            api_key = os.getenv('API_KEY'), 
            api_secret = os.getenv('API_SECRET'))

        return config
    
    def subir_imagen(imagen):
        cloudinary_bd.config_cloudinary()
        res = cloudinary.uploader.upload(imagen)
        url_imagen = res['secure_url']

        return url_imagen

    
    def eliminar_imagen(id_imagen):
        cloudinary_bd.config_cloudinary()
        res = cloudinary.uploader.destroy(id_imagen)
        imagen_eliminada = res['result']

        return imagen_eliminada
