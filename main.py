from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

# init part
db = SQLAlchemy()
jwt = JWTManager()
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
app.config['JWT_QUERY_STRING_NAME'] = jwt

jwt.init_app(app)
db.init_app(app)