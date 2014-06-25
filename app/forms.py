
from flask.ext.wtf import Form
from app import models
from urlparse import urlparse
from wtforms.fields import IntegerField, StringField, FormField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import Optional, InputRequired, ValidationError

def external_url(form, field):
	url = urlparse(field.data)
	if url.scheme not in ('http', 'https') or not url.netloc:
		raise ValidationError('Field must be a valid external URL')


class State(Form):
	hp = IntegerField('HP', [Optional()])
	smile = IntegerField('Smile', [Optional()])
	pure = IntegerField('Pure', [Optional()])
	cool = IntegerField('Cool', [Optional()])
	icon = StringField('Icon', [external_url, Optional()])
	image = StringField('Image', [external_url, Optional()])


class Card(Form):
	id = IntegerField('ID', [InputRequired()])
	name = StringField('Name')

	attribute = SelectField('Attribute',
		choices=[('smile', 'Smile'), ('pure', 'Pure'), ('cool', 'Cool')])

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
