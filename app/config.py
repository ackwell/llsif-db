
import os
appdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Flask 
DEBUG = True

# Database
SQLALCHEMY_DATABASE_URI = "mysql://lovelive:lovelive@localhost/lovelive"
SQLALCHEMY_POOL_RECYCLE = 1
SQLALCHEMY_ECHO = True

# WTForms
CRSF_ENABLED = True
SECRET_KEY = 'secret key'

# Security - Core
SECURITY_URL_PREFIX = '/auth'
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'password salt'

# Security - Features
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True
SECURITY_CHANGEABLE = True

# Assets
ASSETS_DEBUG = DEBUG
LESS_BIN = os.path.join(appdir, 'node_modules', '.bin', 'lessc')

# Uploads
MAX_CONTENT_LENGTH = 2 * 1024 * 1024 # 2MB
UPLOADS_DEFAULT_DEST = os.path.join(appdir, 'app', 'static', 'uploads')
