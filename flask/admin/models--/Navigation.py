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


# Main Classes for app
class Navigation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    link = db.Column(db.String(64))
    download = db.Column(db.String(64), nullable=False)
    open_new_tab = db.Column(db.String(64), nullable=False)

    def __unicode__(self):
        return self.title
