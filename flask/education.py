from sqlalchemy import *

class Education(db.Model):
    def __init__(self, id, school, course, role_bio, key_points, year_of_study, year_of_start):
        id = db.Column(db.Integer, primary_key=True)
        school = db.Column(db.String(100), unique=False, nullable=True)
        course = db.Column(db.String(500), unique=False, nullable=True)
        role_bio = db.Column(db.Text, nullable=True)
        key_points = db.Column(db.Text, nullable=True)
        year_of_study = db.Column(db.Integer, nullable=True)
        year_of_start = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Education('{self.school}','{self.course}')"
