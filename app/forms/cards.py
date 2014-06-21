
from flask.ext.wtf import Form
from wtforms import fields as f

class State(Form):
	hp = f.IntegerField('hp')
	smile = f.IntegerField('smile')
	pure = f.IntegerField('pure')
	cool = f.IntegerField('cool')
	icon = f.FileField('icon')
	image = f.FileField('image')


class Card(Form):
	id = f.IntegerField('id')
	name = f.StringField('name')
	attribute = f.SelectField('attribute', coerce=int)
	rarity = f.SelectField('rarity', coerce=int)

	normal = f.FormField(State)
	idolised = f.FormField(State)

	skill = f.SelectField('skill', coerce=int)
	appeal = f.SelectField('appeal', coerce=int)
