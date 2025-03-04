from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import logging
from flask_sock import Sock
from flask_cors import CORS
# from flask_mail import Mail

app = Flask(__name__, template_folder='./_Admin/templates')
api = Api(app)

# CONNECT TO DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:<password>@localhost/mini_wallet_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# db.init_app(app)
# db.create_all()
migrate = Migrate(app, db)

# LOGGING
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(f"{datetime.utcnow()}")

# Set CORS options on app configuration
app.config['CORS_RESOURCES'] = {r"/*": {"origins": "*"}}
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, supports_credentials=True)

# Sockt
sock = Sock(app)