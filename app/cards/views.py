
from flask import Blueprint, render_template, redirect, url_for
from . import models, forms
from sqlalchemy.exc import IntegrityError

blueprint = Blueprint('cards', __name__, url_prefix='/cards')

######
# Cards
######

@blueprint.route('/')
def index():
	return render_template('cards/index.html',
		cards=models.Card.query.all())


@blueprint.route('/create', methods=['GET', 'POST'], endpoint='create')
@blueprint.route('/edit/<int:card>', methods=['GET', 'POST'], endpoint='edit')
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
			card.normal_state = models.State()
			card.idolised_state = models.State()

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


@blueprint.route('/delete/<int:card>')
def delete(card):
	card = models.Card.query.get(card)
	models.db.session.delete(card)
	models.db.session.commit()
	return redirect(url_for('cards.index'))

######
# Appeals
######

@blueprint.route('/appeals/')
def appeals_index():
	return render_template('appeals/index.html',
		appeals=models.Appeal.query.all())


@blueprint.route('/appeals/create', methods=['GET', 'POST'], endpoint='appeals_create')
@blueprint.route('/appeals/edit/<int:appeal>', methods=['GET', 'POST'], endpoint='appeals_edit')
def appeals_form(appeal=None):
	mode = 'new'
	if appeal is not None:
		appeal = models.Appeal.query.get(appeal)
		mode = 'edit'

	form = forms.Appeal(obj=appeal)

	if form.validate_on_submit():
		if appeal is None:
			appeal = models.Appeal()
		form.populate_obj(appeal)

		models.db.session.add(appeal)
		models.db.session.commit()

		return redirect(url_for('cards.appeals_index'))

	effect_suffix = {
		'None': 'points', # Form defaults to score
		'score': 'points',
		'health': 'HP',
		'perfect': 'seconds'
	}[form.effect.data];

	return render_template('appeals/form.html',
		form=form,
		mode=mode,
		effect_suffix=effect_suffix)


@blueprint.route('/appeals/delete/<int:appeal>')
def appeals_delete(appeal):
	appeal = models.Appeal.query.get(appeal)
	models.db.session.delete(appeal)
	models.db.session.commit()
	return redirect(url_for('cards.appeals_index'))

######
# Skills
######

@blueprint.route('/skills/')
def skills_index():
	return render_template('skills/index.html',
		skills=models.Skill.query.all())


@blueprint.route('/skills/create', methods=['GET', 'POST'], endpoint='skills_create')
@blueprint.route('/skills/edit/<int:skill>', methods=['GET', 'POST'], endpoint='skills_edit')
def skills_form(skill=None):
	mode = 'new'
	if skill is not None:
		skill = models.Skill.query.get(skill)
		mode = 'edit'

	form = forms.Skill(obj=skill)

	if form.validate_on_submit():
		if skill is None:
			skill = models.Skill()
		form.populate_obj(skill)

		models.db.session.add(skill)
		models.db.session.commit()

		return redirect(url_for('cards.skills_index'))

	return render_template('skills/form.html',
		form=form,
		mode=mode)


@blueprint.route('/skills/delete/<int:skill>')
def skills_delete(skill):
	skill = models.Skill.query.get(skill)
	models.db.session.delete(skill)
	models.db.session.commit()
	return redirect(url_for('cards.skills_index'))