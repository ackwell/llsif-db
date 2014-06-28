
from flask import Blueprint, render_template, current_app

controller = Blueprint('home', __name__)

@controller.route('/')
def index():
	return render_template('home/index.html')

current_app.register_blueprint(controller)
