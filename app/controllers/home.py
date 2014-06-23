
from flask import Blueprint, render_template
from app import app

controller = Blueprint('home', __name__)

@controller.route('/')
def index():
	return render_template('home/index.html')

app.register_blueprint(controller)
