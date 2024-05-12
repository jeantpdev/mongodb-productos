from conexiones.conexionCloudinary import *

class consultas_cloudinary:
    
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
