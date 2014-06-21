
from flask import render_template
from app import models

def hello():
	print models.Card.query.all()

	return render_template('hello.html')
