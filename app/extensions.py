
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()
db.Model.metadata = db.MetaData(naming_convention={
	"ix": 'ix_%(column_0_label)s',
	"uq": "uq_%(table_name)s_%(column_0_name)s",
#	"ck": "ck_%(table_name)s_%(constraint_name)s",
	"fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
	"pk": "pk_%(table_name)s"
})

from flask.ext.security import Security
security = Security()

from flask.ext.mail import Mail
mail = Mail()

from flask.ext.assets import Environment
assets = Environment()
