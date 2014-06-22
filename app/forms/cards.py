
from flask.ext.wtf import Form
from wtforms import fields as f
from wtforms import validators as v
from app import models
from urlparse import urlparse

def external_url(form, field):
	url = urlparse(field.data)
	if url.scheme not in ('http', 'https') or not url.netloc:
		raise v.ValidationError('Field must be a valid external URL')


class State(Form):
	hp = f.IntegerField('HP')
	smile = f.IntegerField('Smile')
	pure = f.IntegerField('Pure')
	cool = f.IntegerField('Cool')
	icon = f.StringField('Icon', [external_url])
	image = f.StringField('Image', [external_url])


class Card(Form):
	id = f.IntegerField('ID', [v.InputRequired()])
	name = f.StringField('Name')
	attribute = f.SelectField('Attribute', coerce=int)
	rarity = f.SelectField('Rarity', coerce=int)

	normal = f.FormField(State, label='Normal')
	idolised = f.FormField(State, label='Idolised')

	skill = f.SelectField('Skill', coerce=int)
	appeal = f.SelectField('Appeal', coerce=int)

	def __init__(self, *args, **kwargs):
		super(Card, self).__init__(*args, **kwargs)

		self.attribute.choices = map(
			lambda attr: (attr.id, attr.name,),
			models.Attribute.query.all())

		self.rarity.choices = map(
			lambda rarity: (rarity.id, rarity.name,),
			models.Rarity.query.filter(models.Rarity.id%2 == 1).all())

		self.skill.choices = map(
			lambda skill: (skill.id, skill.name,),
			models.Skill.query.all())

		self.appeal.choices = map(
			lambda appeal: (appeal.id, appeal.name,),
			models.Appeal.query.all())
