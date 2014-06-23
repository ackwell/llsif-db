
from flask import Blueprint, render_template, redirect, url_for
from app import app, models, forms
from sqlalchemy.exc import IntegrityError

controller = Blueprint('cards', __name__)

@controller.route('/')
def index():
	return render_template('cards/index.html',
		cards=models.Card.query.all())


@controller.route('/create', methods=['GET', 'POST'])
def create():
	form = forms.Card()

	# Will only run validations on POST
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

	return render_template('cards/create.html',
		form=form)

app.register_blueprint(controller, url_prefix='/cards')
