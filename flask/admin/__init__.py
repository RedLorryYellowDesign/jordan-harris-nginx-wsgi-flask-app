from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

import admin.main
