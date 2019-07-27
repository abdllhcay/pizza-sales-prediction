from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza-sales-prediction.db'
app.secret_key = "pizza monster"
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from api import routes