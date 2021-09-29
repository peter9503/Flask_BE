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
app.config['JWT_QUERY_STRING_NAME'] = os.getenv('JWT_SECRET')

jwt.init_app(app)
db.init_app(app)