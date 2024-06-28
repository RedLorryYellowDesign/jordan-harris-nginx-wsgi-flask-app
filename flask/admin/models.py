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


# Create directory for file fields to use
file_path = op.join(op.dirname(__file__), 'static/files')
try:
    os.mkdir(file_path)
except OSError:
    pass

# Create user model.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))
    # Flask-Login integration
    # NOTE: is_authenticated, is_active, and is_anonymous
    # are methods in Flask-Login < 0.3.0
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.InputRequired()])
    password = fields.PasswordField(validators=[validators.InputRequired()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(form.Form):
    login = fields.StringField(validators=[validators.InputRequired()])
    email = fields.StringField()
    password = fields.PasswordField(validators=[validators.InputRequired()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')


# MY MODEL VIEWS FOR THE ADMIN DB
# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view')+ '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

# Main Classes for app
class Navigation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    link = db.Column(db.String(64))
    download = db.Column(db.String(64), nullable=False)
    open_new_tab = db.Column(db.String(64), nullable=False)

    def __unicode__(self):
        return self.name


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

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catagory = db.Column(db.String(100), unique=False, nullable=True)
    skill = db.Column(db.String(500), unique=False, nullable=True)
    skill_image = db.Column(db.Unicode(128))
    employment_id = db.Column(db.Integer, db.ForeignKey("employment.id"))

    def __str__(self):
        return "{}".format(self.skill)


class Certifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cert_name = db.Column(db.String(100), unique=False, nullable=False)
    year_of_start = db.Column(db.String(100), unique=False, nullable=True)
    year_of_finish = db.Column(db.String(100), unique=False, nullable=True)
    cert_link = db.Column(db.String(100), unique=False, nullable=True)
    cert_provider = db.Column(db.String(100), unique=False, nullable=True)

    def __unicode__(self):
        return self.name

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), unique=False, nullable=False)
    image_file = db.Column(db.String(20), unique=False, nullable=False,
                default='default.jpg')
    about = db.Column(db.Text, unique=False, nullable=True)

    def __unicode__(self):
        return self.project_name



# Create models
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))

    def __unicode__(self):
        return self.name

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))

    def __unicode__(self):
        return self.name


# Delete hooks for models, delete files if models are getting deleted
@listens_for(File, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            # Don't care if was not deleted because it does not exist
            pass


@listens_for(Image, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        # Delete image
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(op.join(file_path, form.thumbgen_filename(target.path)))
        except OSError:
            pass


# define a custom wtforms widget and field.
# see https://wtforms.readthedocs.io/en/latest/widgets.html#custom-widgets
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        # add WYSIWYG class to existing classes
        existing_classes = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = '{} {}'.format(existing_classes, "ckeditor")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()

class FileView(sqla.ModelView):
    # Override form field to use Flask-Admin FileUploadField
    form_overrides = {
        'path': fl_form.FileUploadField
    }

    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {
        'path': {
            'label': 'File',
            'base_path': file_path,
            'allow_overwrite': True
        }
    }


# Returns and renders Preview of images
class ImageView(sqla.ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                        filename=fl_form.thumbgen_filename('files/'+ model.path)))

    column_formatters = {
        'path': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {'path': fl_form.ImageUploadField('Image',
                                    base_path=file_path,
                                    thumbnail_size=(100, 100, True))
    }


# Returns and renders Preview of images
class SkillView(sqla.ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                        filename=fl_form.thumbgen_filename('files/'+ model.path)))

    column_formatters = {
        'Skill Image': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {'path': fl_form.ImageUploadField('Skills',
                                    base_path=file_path,
                                    thumbnail_size=(100, 100, True))
    }
