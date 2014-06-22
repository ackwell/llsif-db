
from flask import render_template, request, redirect, url_for
from app import models, forms

def index():
	data = dict(
		cards=models.Card.query.all()
	)

	return render_template('cards/index.html', **data)


def create():
	data = dict(
		form=forms.Card()
	)

	return render_template('cards/create.html', **data)


def store():
	form = forms.Card(request.form)

	if form.validate():
		# save
		return redirect(url_for('cards.index'))

	data = dict(
		form=form
	)

	return render_template('cards/create.html', **data)
