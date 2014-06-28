
from flask import Blueprint, render_template, redirect, url_for, current_app
from app import models, forms

controller = Blueprint('skills', __name__)

@controller.route('/')
def index():
	return render_template('skills/index.html',
		skills=models.Skill.query.all())


@controller.route('/create', methods=['GET', 'POST'], endpoint='create')
@controller.route('/edit/<int:skill>', methods=['GET', 'POST'], endpoint='edit')
def form(skill=None):
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

		return redirect(url_for('skills.index'))

	return render_template('skills/form.html',
		form=form,
		mode=mode)


@controller.route('/delete/<int:skill>')
def delete(skill):
	skill = models.Skill.query.get(skill)
	models.db.session.delete(skill)
	models.db.session.commit()
	return redirect(url_for('skills.index'))

current_app.register_blueprint(controller, url_prefix='/skills')
