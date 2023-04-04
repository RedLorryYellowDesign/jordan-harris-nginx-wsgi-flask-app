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
