
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Flask 
DEBUG = True

# Database
SQLALCHEMY_DATABASE_URI = "mysql://lovelive:lovelive@localhost/lovelive"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database')
SQLALCHEMY_ECHO = True
