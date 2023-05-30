from admin import db
from admin.models import *
import random
import datetime
import string



def build_sample_db():
    """
    Populate a small db with some example entries.
    """


    # db.drop_all()
    # db.create_all()
    # # passwords are hashed, to use plaintext passwords instead:
    # test_user = User(login="test", password="test")

    # # make user acount -- Hash out once built
    # test_user = User(login="test",email='test@test.com',
    # password=generate_password_hash("test"))
    # db.session.add(test_user)

    # # make Education -- Hash out once built
    # test_school = Education(school="test", course="test")
    # db.session.add(test_school)

    # # make Employment -- Hash out once built
    # test_employer = Employment(employer="test", role="test")
    # db.session.add(test_employer)

    # # make Employment -- Hash out once built
    # my_bio = MyInfo(email="test")
    # db.session.add(my_bio)


    # images = ["Buffalo", "Elephant", "Leopard", "Lion", "Rhino"]
    # for name in images:
    #     image = Image()
    #     image.name = name
    #     image.path = name.lower() + ".jpg"
    #     db.session.add(image)

    # for i in [1, 2, 3]:
    #     file = File()
    #     file.name = "Example " + str(i)
    #     file.path = "example_" + str(i) + ".pdf"
    #     db.session.add(file)

    db.session.commit()
    return
