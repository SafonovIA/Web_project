from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:12345@localhost:5435/my_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '2265bd9fc3b479d702abfd245ea071be'
db = SQLAlchemy(app)
