
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.security import login_required, current_user
from sqlalchemy.exc import IntegrityError
from PIL import Image
from . import models, forms
from ..util import DeleteForm
from ..users import ActionLog
from ..extensions import db
from ..uploads import card_images
import os

blueprint = Blueprint('cards', __name__, url_prefix='/cards')

######
# Cards
######

@blueprint.route('/')
def index():
	return render_template('cards/index.html',
		cards=models.Card.query.all(),
		card_images=card_images)


@blueprint.route('/create', methods=['GET', 'POST'], endpoint='create')
@blueprint.route('/edit/<int:card>', methods=['GET', 'POST'], endpoint='edit')
@login_required
def form(card=None):
	mode = 'new'
	if card is not None:
		card = models.Card.query.get_or_404(card)
		card.rarity = card.normal_state.rarity
		mode = 'edit'

	form = forms.Card(obj=card)

	# Will only run validations on POST
	if form.validate_on_submit():
		# Populate
		if card is None:
			card = models.Card()
			card.normal_state = models.State()
			card.idolised_state = models.State()

		# Handle files if available
		for state_name in ['normal_state', 'idolised_state']:
			field = getattr(form, state_name).icon

			if field.data:
				# There is an uploaded file, save then resize with Pillow
				filename = card_images.save(field.data,
					name='%s_%s_icon.' % (card.id, state_name,))

				# Someone should murder me for writing this bullshit.
				# Why is this even in a fucking controller?
				# TODO: Move all this Pillow bullshit into a separate file.
				infile = card_images.path(filename)
				filename = os.path.splitext(filename)[0] + '.jpg'
				outfile = card_images.path(filename)

				image = Image.open(infile)

				new_size = (138, 184)
				cur_ratio = image.size[0] / float(image.size[1])
				new_ratio = new_size[0] / float(new_size[1])

				if new_ratio > cur_ratio:
					image = image.resize((new_size[0], int(round(new_size[0] * image.size[1] / image.size[0]))), Image.ANTIALIAS)
					image = image.crop((0, int(round((image.size[1] - new_size[1]) / 2)), image.size[0], int(round((image.size[1] + new_size[1]) / 2))))
				elif new_ratio < cur_ratio:
					image = image.resize((int(round(new_size[1] * image.size[0] / image.size[1])), new_size[1]), Image.ANTIALIAS)
					image.crop((int(round((image.size[0] - new_size[0]) / 2)), 0, int(round((image.size[0] + new_size[0]) / 2)), image.size[1]))
				else :
					image = image.resize((new_size[0], new_size[1]), Image.ANTIALIAS)

				image.save(outfile, 'JPEG', quality=80)

				if infile != outfile:
					os.remove(infile)

				field.data = filename
			else:
				# No uploaded file, save the previous data from the model
				field.data = getattr(card, state_name).icon

		form.populate_obj(card)

		# Set the state rarities
		rarity = form.rarity.data
		card.normal_state.rarity = rarity
		card.idolised_state.rarity = models.Rarity.query.get(rarity.id + 1)

		# Save, catching ID duplicates
		# (Not using a verifier, it'd double the SQL queries, and be a general PITA)
		db.session.add(card)
		try:
			db.session.commit()
		except IntegrityError:
			form.id.errors.append('The specified ID already exists.')
			db.session.rollback()
		else:
			log = ActionLog(
				user=current_user,
				action='card.%s(%s)'%(mode, card.id))
			db.session.add(log)
			db.session.commit()

			return redirect(url_for('cards.index'))

	return render_template('cards/form.html',
		form=form,
		mode=mode)


@blueprint.route('/delete/<int:card>', methods=['POST'])
@login_required
def delete(card):
	form = DeleteForm()

	if form.validate_on_submit():
		card = models.Card.query.get_or_404(card)
		db.session.delete(card)
		db.session.commit()

		log = ActionLog(
			user=current_user,
			action='card.delete(%s)'%(card.id))
		db.session.add(log)
		db.session.commit()

	return redirect(url_for('cards.index'))

######
# Appeals
######

@blueprint.route('/appeals/')
def appeals_index():
	return render_template('cards/appeals/index.html',
		appeals=models.Appeal.query.all())


@blueprint.route('/appeals/create', methods=['GET', 'POST'], endpoint='appeals_create')
@blueprint.route('/appeals/edit/<int:appeal>', methods=['GET', 'POST'], endpoint='appeals_edit')
@login_required
def appeals_form(appeal=None):
	mode = 'new'
	if appeal is not None:
		appeal = models.Appeal.query.get_or_404(appeal)
		mode = 'edit'

	form = forms.Appeal(obj=appeal)

	if form.validate_on_submit():
		if appeal is None:
			appeal = models.Appeal()
		form.populate_obj(appeal)

		db.session.add(appeal)
		db.session.commit()

		log = ActionLog(
			user=current_user,
			action='card.appeal.%s(%s)'%(mode, appeal.id))
		db.session.add(log)
		db.session.commit()

		return redirect(url_for('cards.appeals_index'))

	effect_suffix = {
		'score': 'points',
		'health': 'HP',
		'perfect': 'seconds'
	}.get(form.effect.data)

	return render_template('cards/appeals/form.html',
		form=form,
		mode=mode,
		effect_suffix=effect_suffix)


@blueprint.route('/appeals/delete/<int:appeal>', methods=['POST'])
@login_required
def appeals_delete(appeal):
	form = DeleteForm()

	if form.validate_on_submit():
		appeal = models.Appeal.query.get_or_404(appeal)
		db.session.delete(appeal)
		db.session.commit()

		log = ActionLog(
			user=current_user,
			action='card.appeal.delete(%s)'%(appeal.id))
		db.session.add(log)
		db.session.commit()

	return redirect(url_for('cards.appeals_index'))

######
# Skills
######

@blueprint.route('/skills/')
def skills_index():
	return render_template('cards/skills/index.html',
		skills=models.Skill.query.all())


@blueprint.route('/skills/create', methods=['GET', 'POST'], endpoint='skills_create')
@blueprint.route('/skills/edit/<int:skill>', methods=['GET', 'POST'], endpoint='skills_edit')
@login_required
def skills_form(skill=None):
	mode = 'new'
	if skill is not None:
		skill = models.Skill.query.get_or_404(skill)
		mode = 'edit'

	form = forms.Skill(obj=skill)

	if form.validate_on_submit():
		if skill is None:
			skill = models.Skill()
		form.populate_obj(skill)

		db.session.add(skill)
		db.session.commit()

		log = ActionLog(
			user=current_user,
			action='card.skill.%s(%s)'%(mode, skill.id))
		db.session.add(log)
		db.session.commit()

		return redirect(url_for('cards.skills_index'))

	return render_template('cards/skills/form.html',
		form=form,
		mode=mode)


@blueprint.route('/skills/delete/<int:skill>', methods=['POST'])
@login_required
def skills_delete(skill):
	form = DeleteForm()

	if form.validate_on_submit():
		skill = models.Skill.query.get_or_404(skill)
		db.session.delete(skill)
		db.session.commit()

		log = ActionLog(
			user=current_user,
			action='card.skill.delete(%s)'%(skill.id))
		db.session.add(log)
		db.session.commit()

	return redirect(url_for('cards.skills_index'))
