from librerias import *
from rutas.rutas_productos import *

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# GENERALES
app.register_blueprint(todo)

#Pagina de error
def pagina_no_encontrada(error):
    return "<h1>La pagina a la que intentas acceder no existe...</h1>"

if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    app.run(host="0.0.0.0",port = 5900, debug=True)