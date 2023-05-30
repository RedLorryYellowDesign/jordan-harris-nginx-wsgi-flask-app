class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), unique=False, nullable=False)
    image_file = db.Column(db.String(20), unique=False, nullable=False,
                default='default.jpg')
    about = db.Column(db.Text, unique=False, nullable=True)

    def __unicode__(self):
        return self.project_name
