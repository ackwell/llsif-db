
from flask import render_template
from app import models, forms

def index():
	data = dict()
	data['cards'] = models.Card.query.all()

	return render_template('cards/index.html', **data)


def new():
	form = forms.Card()

	form.attribute.choices = map(
		lambda attr: (attr.id, attr.name,),
		models.Attribute.query.all())

	form.rarity.choices = map(
		lambda rarity: (rarity.id, rarity.name,),
		models.Rarity.query.filter(models.Rarity.id%2 == 1).all())

	form.skill.choices = map(
		lambda skill: (skill.id, skill.name,),
		models.Skill.query.all())

	form.appeal.choices = map(
		lambda appeal: (appeal.id, appeal.name,),
		models.Appeal.query.all())

	data = dict()
	data['form'] = form

	return render_template('cards/new.html', **data)
