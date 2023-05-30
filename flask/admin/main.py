
from admin import app, db
from admin.models import *  #MyAdminIndexView, MyModelView, RegistrationForm, LoginForm, User, MyInfo, Education, Employment, Certifications, Projects, File, Image, Navigation, Skills
from flask import render_template
import flask_login as login


# Flask views
@app.route('/static', methods=('GET', 'POST'))
def index_static():
    myinfo = MyInfo
    education = Education
    employment = Employment
    projects = Projects

    return render_template('index.html',
                            myinfo = myinfo.query.all(),
                            education = education.query.all(),
                            employment = employment.query.all(),
                            projects = projects.query.all()
                            )

@app.route('/', methods=('GET', 'POST'))
def index():
    myinfo = MyInfo
    education = Education
    employment = Employment
    certifications = Certifications
    projects = Projects
    navigation = Navigation
    skills = Skills



    return render_template('index_test.html',
                            myinfo = myinfo.query.all(),
                            education = education.query.all(),
                            employment = employment.query.all(),
                            projects = projects.query.all(),
                            certifications = certifications.query.all(),
                            navigation = navigation.query.all(),
                            skills = skills.query.all(),
                            BIM_Tools = skills.query.filter_by(catagory = 'BIM Tools').all(),
                            Design_Tools = skills.query.filter_by(catagory = 'Design Tools').all(),
                            Management_Tools = skills.query.filter_by(catagory = 'Management').all(),
                            Data_Science_Tools = skills.query.filter_by(catagory = 'Data Science').all(),
                            Cloud_Tools = skills.query.filter_by(catagory = 'Cloud').all(),
                            Web_Dev_Tools = skills.query.filter_by(catagory = 'Web Dev').all(),
                            )


@app.route('/projects', methods=('GET', 'POST'))
def projects():
    myinfo = MyInfo
    education = Education
    employment = Employment
    certifications = Certifications
    projects = Projects
    navigation = Navigation
    skills = Skills

    return render_template('projects.html',
                            myinfo = myinfo.query.all(),
                            education = education.query.all(),
                            employment = employment.query.all(),
                            projects = projects.query.all(),
                            certifications = certifications.query.all(),
                            navigation = navigation.query.all(),
                            skills = skills.query.all(),
                            BIM_Tools = skills.query.filter_by(catagory = 'BIM Tools').all(),
                            Design_Tools = skills.query.filter_by(catagory = 'Design Tools').all(),
                            Management_Tools = skills.query.filter_by(catagory = 'Management').all(),
                            Data_Science_Tools = skills.query.filter_by(catagory = 'Data Science').all(),
                            Cloud_Tools = skills.query.filter_by(catagory = 'Cloud').all(),
                            Web_Dev_Tools = skills.query.filter_by(catagory = 'Web Dev').all(),
                            )






# class UserAdmin(sqla.ModelView):

#     can_view_details = True  # show a modal dialog with records details
#     action_disallowed_list = ['delete', ]

#     form_choices = {
#         'type': AVAILABLE_USER_TYPES,
#     }
#     form_args = {
#         'dialling_code': {'label': 'Dialling code'},
#         'local_phone_number': {
#             'label': 'Phone number',
#             'validators': [is_numberic_validator]
#         },
#     }
#     form_widget_args = {
#         'id': {
#             'readonly': True
#         }
#     }
#     column_list = [
#         'type',
#         'first_name',
#         'last_name',
#         'email',
#         'ip_address',
#         'currency',
#         'timezone',
#         'phone_number',
#     ]
#     column_searchable_list = [
#         'first_name',
#         'last_name',
#         'phone_number',
#         'email',
#     ]
#     column_editable_list = ['type', 'currency', 'timezone']
#     column_details_list = [
#         'id',
#         'featured_post',
#         'website',
#         'enum_choice_field',
#         'sqla_utils_choice_field',
#         'sqla_utils_enum_choice_field',
#     ] + column_list
#     form_columns = [
#         'id',
#         'type',
#         'featured_post',
#         'enum_choice_field',
#         'sqla_utils_choice_field',
#         'sqla_utils_enum_choice_field',
#         'last_name',
#         'first_name',
#         'email',
#         'website',
#         'dialling_code',
#         'local_phone_number',
#     ]
#     form_create_rules = [
#         'last_name',
#         'first_name',
#         'type',
#         'email',
#     ]

#     column_auto_select_related = True
#     column_default_sort = [('last_name', False), ('first_name', False)]  # sort on multiple columns

#     # custom filter: each filter in the list is a filter operation (equals, not equals, etc)
#     # filters with the same name will appear as operations under the same filter
#     column_filters = [
#         'first_name',
#         FilterEqual(column=User.last_name, name='Last Name'),
#         FilterLastNameBrown(column=User.last_name, name='Last Name',
#                             options=(('1', 'Yes'), ('0', 'No'))),
#         'phone_number',
#         'email',
#         'ip_address',
#         'currency',
#         'timezone',
#     ]
#     column_formatters = {'phone_number': phone_number_formatter}

#     # setup edit forms so that only posts created by this user can be selected as 'featured'
#     def edit_form(self, obj):
#         return self._filtered_posts(
#             super(UserAdmin, self).edit_form(obj)
#         )

#     def _filtered_posts(self, form):
#         form.featured_post.query_factory = lambda: Post.query.filter(Post.user_id == form._obj.id).all()
#         return form


# Customized Post model admin
class EmploymentAdmin(sqla.ModelView):
    # column_display_pk = True
    # column_list = ['id', 'user', 'title', 'date', 'tags', 'background_color', 'created_at', ]
    # column_editable_list = ['background_color', ]
    # column_default_sort = ('date', True)
    create_modal = True
    edit_modal = True
    # column_sortable_list = [
    #     'id',
    #     'title',
    #     'date',
    #     ('user', ('user.last_name', 'user.first_name')),  # sort on multiple columns
    # ]
    # column_labels = {
    #     'title': 'Post Title'  # Rename 'title' column in list view
    # }
    # column_searchable_list = [
    #     'title',
    #     'tags.name',
    #     'user.first_name',
    #     'user.last_name',
    # ]
    # column_labels = {
    #     'title': 'Title',
    #     'tags.name': 'Tags',
    #     'user.first_name': 'User\'s first name',
    #     'user.last_name': 'Last name',
    #}
    # column_filters = [
    #     'id',
    #     'user.first_name',
    #     'user.id',
    #     'background_color',
    #     'created_at',
    #     'title',
    #     'date',
    #     'tags',
    #     filters.FilterLike(Post.title, 'Fixed Title', options=(('test1', 'Test 1'), ('test2', 'Test 2'))),
    # ]
    can_export = True
    export_max_rows = 1000
    export_types = ['csv', 'xls']

    # # Pass arguments to WTForms. In this case, change label for text field to
    # # be 'Big Text' and add DataRequired() validator.
    # form_args = {
    #     'text': dict(label='Big Text', validators=[validators.DataRequired()])
    # }
    # form_widget_args = {
    #     'text': {
    #         'rows': 10
    #     }
    # }

    form_ajax_refs = {
        'skills_used': {
            'fields': (Skills.skill,),
            'minimum_input_length': 0,  # show suggestions, even before any user input
            'placeholder': 'Please select',
            'page_size': 5,
        },
    }

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'Example: Auth', index_view=MyAdminIndexView(),
                    base_template='my_master.html', template_mode='bootstrap4')



# Declares views shown is Admin Consle
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Education, db.session))
admin.add_view(FileView(Projects, db.session))
admin.add_view(EmploymentAdmin(Employment, db.session))
admin.add_view(ImageView(MyInfo, db.session))
admin.add_view(MyModelView(Certifications, db.session))
admin.add_view(FileView(File, db.session))
admin.add_view(ImageView(Image, db.session))
admin.add_view(FileView(Navigation, db.session))
admin.add_view(SkillView(Skills, db.session))
