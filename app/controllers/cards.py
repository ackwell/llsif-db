
from flask import render_template
from app import models

def index():
	data = dict()

	data['cards'] = models.Card.query.all()

	return render_template('cards/index.html', **data)
