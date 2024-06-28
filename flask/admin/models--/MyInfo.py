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

class MyInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    born = db.Column(db.Integer, unique=True)
    tag_line = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    linkedin = db.Column(db.String(64))
    linkedin_username = db.Column(db.String(64))
    github = db.Column(db.String(64))
    github_username = db.Column(db.String(64))
    my_bio = db.Column(db.Text, nullable=True)
    my_overview = db.Column(db.Text, nullable=True)
    more_indepth = db.Column(db.Text, nullable=True)
    path = db.Column(db.Unicode(128))
    titles = db.Column(db.Unicode(128))
    tagline = db.Column(db.Unicode(128))
    my_location = db.Column(db.Unicode(128))

    def __unicode__(self):
        return self.name
