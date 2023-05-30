from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__, static_folder='static')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

import admin.main



# import os
# from flask import Flask
# from dotenv import load_dotenv
# #...

# # load dotenv in the base root
# APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)

# app.config = os.getenv('SECRET_KEY')
