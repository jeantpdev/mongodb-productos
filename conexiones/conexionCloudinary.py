import cloudinary
import cloudinary.uploader
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
