from flask import Flask
from routes.eventos import eventos
from models import db


app = Flask(__name__)

# cargar archivo de configuracion de la aplicacion
app.config.from_object('config')

# inicializar base de datos
db.app = app
db.init_app(app)


app.register_blueprint(eventos)




