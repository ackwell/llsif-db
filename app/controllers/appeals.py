
from flask import Blueprint, render_template, current_app
from app import models, forms

controller = Blueprint('appeals', __name__)

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

		# Should probably do more here... not that it'll really be accessed without ajax
		return 'saved'

	effect_suffix = {
		'score': 'points',
		'health': 'HP',
		'perfect': 'seconds'
	}[form.effect.data];

	return render_template('appeals/form.html',
		form=form,
		mode=mode,
		effect_suffix=effect_suffix)

current_app.register_blueprint(controller, url_prefix='/appeals')
