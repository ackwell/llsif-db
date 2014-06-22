
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Flask 
DEBUG = True

# Database
SQLALCHEMY_DATABASE_URI = "mysql://lovelive:lovelive@localhost/lovelive"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database')
SQLALCHEMY_POOL_RECYCLE = 1
SQLALCHEMY_ECHO = True

# WTForms
CRSF_ENABLED = True
SECRET_KEY = 'secret key'
