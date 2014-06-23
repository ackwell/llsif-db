
from flask import render_template, redirect, url_for
from app import models, forms
from sqlalchemy.exc import IntegrityError

def index():
	data = dict(
		cards=models.Card.query.all()
	)

	return render_template('cards/index.html', **data)


def create():
	form = forms.Card()

	if form.validate_on_submit():
		# Populate
		card = models.Card()
		form.populate_obj(card)

		# Set the state rarities
		rarity = form.rarity.data
		card.normal_state.rarity = rarity
		card.idolised_state.rarity = models.Rarity.query\
			.filter(models.Rarity.id == rarity.id + 1).first()

		# Save, catching ID duplicates
		# (Not using a verifier, it'd double the SQL queries, and be a general PITA)
		models.db.session.add(card)
		try:
			models.db.session.commit()
		except IntegrityError:
			form.id.errors.append('The specified ID already exists.')
			models.db.session.rollback()
		else:
			return redirect(url_for('cards.index'))

	data = dict(
		form = form
	)

	return render_template('cards/create.html', **data)
