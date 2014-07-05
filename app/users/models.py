
from ..extensions import db
from flask.ext.security import UserMixin, RoleMixin, SQLAlchemyUserDatastore

user_roles = db.Table('user_roles',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class User(db.Model, UserMixin):
	# Usual shit
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))

	# Banning / registration email thing
	active = db.Column(db.Boolean)
	confirmed_at = db.Column(db.DateTime)

	# Big brother
	last_login_at = db.Column(db.DateTime)
	current_login_at = db.Column(db.DateTime)
	last_login_ip = db.Column(db.String(16))
	current_login_ip = db.Column(db.String(16))
	login_count = db.Column(db.Integer)

	roles = db.relationship('Role',
		secondary=user_roles,
		backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	description = db.Column(db.String(255))

security_datastore = SQLAlchemyUserDatastore(db, User, Role)
