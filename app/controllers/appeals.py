
from flask import Blueprint, render_template, redirect, url_for, current_app
from app import models, forms

controller = Blueprint('appeals', __name__)

@controller.route('/')
def index():
	return render_template('appeals/index.html',
		appeals=models.Appeal.query.all())


@controller.route('/create', methods=['GET', 'POST'], endpoint='create')
@controller.route('/edit/<int:appeal>', methods=['GET', 'POST'], endpoint='edit')
def form(appeal=None):
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

		return redirect(url_for('appeals.index'))

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


@controller.route('/delete/<int:appeal>')
def delete(appeal):
	appeal = models.Appeal.query.get(appeal)
	models.db.session.delete(appeal)
	models.db.session.commit()
	return redirect(url_for('appeals.index'))

current_app.register_blueprint(controller, url_prefix='/appeals')
