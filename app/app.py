
from flask import Flask, request
from .extensions import db
from . import home, cards

__all__ = ['create_app']

def create_app():
	app = Flask(__name__)
	app.config.from_object('app.config')

	# Set up application
	configure_blueprints(app)
	configure_extensions(app)

	return app

def configure_blueprints(app):
	app.register_blueprint(home.blueprint)
	app.register_blueprint(cards.blueprint)

def configure_extensions(app):
	db.init_app(app)