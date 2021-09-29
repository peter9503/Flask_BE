from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# init part
db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')

db.init_app(app)