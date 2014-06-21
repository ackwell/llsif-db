
from flask import render_template
from app import models

def hello():
	data = dict()

	data['cards'] = models.Card.query.all()

	return render_template('hello.html', **data)
