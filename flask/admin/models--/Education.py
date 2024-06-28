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


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(100), unique=False, nullable=True)
    course = db.Column(db.String(500), unique=False, nullable=True)
    role_bio = db.Column(db.Text, nullable=True)
    key_points = db.Column(db.Text, nullable=True)
    year_of_study = db.Column(db.Integer, nullable=True)
    year_of_start = db.Column(db.Integer, nullable=True)

    def __unicode__(self):
        return self.name
