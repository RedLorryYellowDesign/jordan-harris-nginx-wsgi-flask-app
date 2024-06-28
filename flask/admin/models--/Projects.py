# From Local App
from admin import db, app
# from admin.models import User
# Allowing for interaction on local device.
import os
import os.path as op
# Flask Imports
from flask import url_for, redirect, request
from sqlalchemy.event import listens_for
from markupsafe import Markup
import flask_admin as admin
from flask_admin import form as fl_form
import flask_login as login
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import fields, validators, widgets, form

from models import *


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), unique=False, nullable=False)
    image_file = db.Column(db.String(20), unique=False, nullable=False,
                default='default.jpg')
    about = db.Column(db.Text, unique=False, nullable=True)

    def __unicode__(self):
        return self.project_name
