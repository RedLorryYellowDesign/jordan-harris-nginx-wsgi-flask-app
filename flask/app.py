import os
from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

from wtforms import form, fields, validators
import flask_admin as admin
import flask_login as login
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash
from education import Education
# from admin import admin




# Create Flask application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['DATABASE_FILE'] = 'sample_db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

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


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


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
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
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

    @expose('/update_db/')
    def logout_view(self):

        return redirect(url_for('.index'))

# Main Classes for app
class MyInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    born = db.Column(db.String(80), unique=True)
    tagline = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    linkedin = db.Column(db.String(64))
    github = db.Column(db.String(64))
    my_bio = db.Column(db.Text, nullable=True)
    my_overview = db.Column(db.Text, nullable=True)
    more_indepth = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"MyInfo('{self.phone}')"





class InternshipMentoring(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer = db.Column(db.String(100), unique=False, nullable=True)
    role = db.Column(db.String(500), unique=False, nullable=True)
    role_bio = db.Column(db.Text, nullable=True)
    key_points = db.Column(db.Text, nullable=True)
    year_of_study = db.Column(db.Integer, nullable=True)
    year_of_start = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Employment('{self.employer}','{self.role}')"


class Education(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        school = db.Column(db.String(100), unique=False, nullable=True)
        course = db.Column(db.String(500), unique=False, nullable=True)
        role_bio = db.Column(db.Text, nullable=True)
        key_points = db.Column(db.Text, nullable=True)
        year_of_study = db.Column(db.Integer, nullable=True)
        year_of_start = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Education('{self.school}','{self.course}')"



class Employment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer = db.Column(db.String(100), unique=False, nullable=True)
    role = db.Column(db.String(500), unique=False, nullable=True)
    role_bio = db.Column(db.Text, nullable=True)
    key_points = db.Column(db.Text, nullable=True)
    year_of_study = db.Column(db.Integer, nullable=True)
    year_of_start = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Employment('{self.employer}','{self.role}')"




class Employment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer = db.Column(db.String(100), unique=False, nullable=True)
    role = db.Column(db.String(500), unique=False, nullable=True)
    role_bio = db.Column(db.Text, nullable=True)
    key_points = db.Column(db.Text, nullable=True)
    year_of_study = db.Column(db.Integer, nullable=True)
    year_of_start = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Employment('{self.employer}','{self.role}')"



class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), unique=False, nullable=False)
    image_file = db.Column(db.String(20), unique=False, nullable=False, default='default.jpg')
    about = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f"Projects('{self.project_name}')"




# Flask views
@app.route('/', methods=('GET', 'POST'))
def index():
    education = Education
    employment = Employment
    myinfo = MyInfo
    return render_template('index2.html',education = education.query.all(),myinfo = myinfo.query.all(), employment = employment.query.all())

# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'Example: Auth', index_view=MyAdminIndexView(), base_template='my_master.html', template_mode='bootstrap4')

# Add view
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Education, db.session))
admin.add_view(MyModelView(Projects, db.session))
admin.add_view(MyModelView(Employment, db.session))
admin.add_view(MyModelView(MyInfo, db.session))

@app.route('/build', methods=('GET', 'POST'))
def build_sample_db():
    """
    Populate a small db with some example entries.
    """

    import string
    import random

    # db.drop_all()
    db.create_all()
    # # passwords are hashed, to use plaintext passwords instead:
    # test_user = User(login="test", password="test")

    # # make user acount -- Hash out once built
    # test_user = User(login="test",email='test@test.com', password=generate_password_hash("test"))
    # db.session.add(test_user)

    # # make Education -- Hash out once built
    # test_school = Education(school="test", course="test")
    # db.session.add(test_school)

    # # make Employment -- Hash out once built
    # test_employer = Employment(employer="test", role="test")
    # db.session.add(test_employer)

    # make Employment -- Hash out once built
    my_bio = MyInfo(email="test")
    db.session.add(my_bio)


    db.session.commit()
    return "pingpong"





if __name__ == '__main__':

    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        with app.app_context():
            build_sample_db()

    #Start app
    app.run(debug=True)
