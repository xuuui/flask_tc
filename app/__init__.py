import gevent.monkey
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_socketio import SocketIO
from config import config
gevent.monkey.patch_all()

app = Flask(__name__)
app.config.from_object(config['Production'])
CORS(app, supports_credentials=True)
socketio = SocketIO(app)
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from .main import main as main_bluereprint
app.register_blueprint(main_bluereprint, url_prefix='/flask/')
from .api import api as api_bluereprint
app.register_blueprint(api_bluereprint, url_prefix='/flask/api')

from . import models