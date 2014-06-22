
from flask.ext.wtf import Form
from wtforms import fields as f

class State(Form):
	hp = f.IntegerField('HP')
	smile = f.IntegerField('Smile')
	pure = f.IntegerField('Pure')
	cool = f.IntegerField('Cool')
	icon = f.FileField('Icon')
	image = f.FileField('Image')


class Card(Form):
	id = f.IntegerField('ID')
	name = f.StringField('Name')
	attribute = f.SelectField('Attribute', coerce=int)
	rarity = f.SelectField('Rarity', coerce=int)

	normal = f.FormField(State, label='Normal')
	idolised = f.FormField(State, label='Idolised')

	skill = f.SelectField('Skill', coerce=int)
	appeal = f.SelectField('Appeal', coerce=int)
