
from flask.ext.wtf import Form
from urlparse import urlparse
from wtforms.fields import IntegerField, StringField, FormField, SelectField, DecimalField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import Optional, InputRequired, NumberRange, ValidationError
from . import models

# Stuff I reuse
attributes = [('smile', 'Smile'), ('pure', 'Pure'), ('cool', 'Cool')]

# Validators
def external_url(form, field):
	url = urlparse(field.data)
	if url.scheme not in ('http', 'https') or not url.netloc:
		raise ValidationError('Field must be a valid external URL')


# Forms
class State(Form):
	hp = IntegerField('HP', [Optional()])
	smile = IntegerField('Smile', [Optional()])
	pure = IntegerField('Pure', [Optional()])
	cool = IntegerField('Cool', [Optional()])
	icon = StringField('Icon', [external_url, Optional()])
	image = StringField('Image', [external_url, Optional()])


class Card(Form):
	id = IntegerField('ID', [InputRequired()])
	name = StringField('Name', [InputRequired()])

	attribute = SelectField('Attribute', choices=attributes)

	rarity = QuerySelectField('Rarity',
		query_factory=lambda: models.Rarity.query.filter(models.Rarity.id%2 == 1).all())

	normal_state = FormField(State, default=models.State(), label='Normal')
	idolised_state = FormField(State, default=models.State(), label='Idolised')

	skill = QuerySelectField('Skill',
		query_factory=lambda: models.Skill.query.all())
	appeal = QuerySelectField('Appeal',
		query_factory=lambda: models.Appeal.query.all())

	availability = QuerySelectMultipleField('Availability',
		query_factory=lambda: models.Region.query.all())


class Skill(Form):
	name = StringField('Name', [InputRequired()])
	description = StringField('Description')

	bonus_attribute = SelectField('Bonus Attribute', choices=attributes)
	scale_attribute = SelectField('Scale Attribute', choices=attributes)
	scale = IntegerField('Scale', [InputRequired(), NumberRange(0, 100)])


class Appeal(Form):
	name = StringField('Name', [InputRequired()])
	description = StringField('Description')

	effect = SelectField('Effect',
		choices=[('score', 'Score Boost'), ('health', 'Health Regen'), ('perfect', 'Perfect Lock')])
	effect_modifier = DecimalField('Effect Modifier')

	proc_statistic = SelectField('Proc Statistic',
		choices=[ ('seconds', 'Seconds'), ('notes', 'Notes'), ('combo', 'Combo'), ('perfects', 'Perfects'), ('score', 'Score')])
	proc_count = IntegerField('Proc Count')
	proc_chance = IntegerField('Proc Chance', [NumberRange(0, 100)])
