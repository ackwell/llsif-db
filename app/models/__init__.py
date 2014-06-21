
from app import app
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from app.models.cards import *
