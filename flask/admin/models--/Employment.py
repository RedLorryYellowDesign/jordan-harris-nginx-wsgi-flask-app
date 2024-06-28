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


skills_tag = db.Table('skills_tag', db.Model.metadata,
                    db.Column('employment_id', db.Integer, db.ForeignKey('employment.id')),
                    db.Column('skills_id', db.Integer, db.ForeignKey('skills.id'))
                    )

class Employment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer = db.Column(db.String(100), unique=False, nullable=True)
    role = db.Column(db.String(500), unique=False, nullable=True)
    role_bio = db.Column(db.Text, nullable=True)
    company_link =  db.Column(db.String(500), unique=False, nullable=True)
    key_points = db.Column(db.Text, nullable=True)
    date_started  = db.Column(db.Unicode(128))
    date_finished  = db.Column(db.Unicode(128))
    path = db.Column(db.Unicode(128))
    target = db.Column(db.Unicode(128))
    # Foren Key
    skills_used = db.relationship('Skills', secondary=skills_tag)


    def __str__(self):
        return "{}".format(self.skills_used)
