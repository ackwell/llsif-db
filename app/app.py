
from flask import Flask, request
from .extensions import db, security, mail
from .context_processor import context_processor
from . import home, cards, users

__all__ = ['create_app']

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object('app.config')
	app.config.from_pyfile('config.py', silent=True)

	# Set up application
	configure_blueprints(app)
	configure_extensions(app)

	app.context_processor(context_processor)

	return app

def configure_blueprints(app):
	app.register_blueprint(home.blueprint)
	app.register_blueprint(cards.blueprint)

def configure_extensions(app):
	db.init_app(app)

	security.init_app(app, users.security_datastore, **users.security_forms)

	mail.init_app(app)
