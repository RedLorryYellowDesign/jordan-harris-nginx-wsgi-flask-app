from dotenv import load_dotenv
import os
# set optional bootswatch theme
# see http://bootswatch.com/3/ for available swatches
FLASK_ADMIN_SWATCH = 'litera'

# Create dummy secrey key so we can use sessions
def configure():
    load_dotenv()

configure()
# Create in-memory database
DATABASE_FILE = 'sample_db.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
