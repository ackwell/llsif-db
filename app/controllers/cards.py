
from flask import Blueprint, render_template, redirect, url_for
from app import app, models, forms
from sqlalchemy.exc import IntegrityError

controller = Blueprint('cards', __name__)

@controller.route('/')
def index():
	return render_template('cards/index.html',
		cards=models.Card.query.all())


@controller.route('/create', methods=['GET', 'POST'], endpoint='create')
@controller.route('/edit/<int:card>', methods=['GET', 'POST'], endpoint='edit')
def form(card=None):
	mode = 'new'
	if card is not None:
		card = models.Card.query.get(card)
		mode = 'edit'

	form = forms.Card(obj=card)

	# Will only run validations on POST
	if form.validate_on_submit():
		# Populate
		if card is None:
			card = models.Card()
		form.populate_obj(card)

		# Set the state rarities
		rarity = form.rarity.data
		card.normal_state.rarity = rarity
		card.idolised_state.rarity = models.Rarity.query.get(rarity.id + 1)

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

	return render_template('cards/form.html',
		form=form,
		mode=mode)


@controller.route('/delete/<int:card>')
def delete(card):
	card = models.Card.query.get(card)
	models.db.session.delete(card)
	models.db.session.commit()
	return redirect(url_for('cards.index'))

app.register_blueprint(controller, url_prefix='/cards')
