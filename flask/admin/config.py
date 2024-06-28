from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()
import os
# set optional bootswatch theme
# see http://bootswatch.com/3/ for available swatches
FLASK_ADMIN_SWATCH = 'litera'
# Create in-memory database
SECRET_KEY = os.getenv('KEY')
DATABASE_FILE = 'sample_db.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
