
from flask.ext.wtf import Form
from flask.ext.security.forms import RegisterForm
from wtforms.fields import PasswordField, StringField, TextAreaField, BooleanField
from wtforms.validators import EqualTo, Length, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..cards import Region

# Because the developer of Flask-Security seriously thinks that
# having email confirmation is a reason to not have password confirmation.
# Fucking retard.
class RegisterFormWithAFuckingPasswordConfirmField(RegisterForm):
	password_confirm = PasswordField('Confirm Password', [EqualTo('password')])


class Account(Form):
	region = QuerySelectField('Region',
		query_factory=lambda: Region.query.all())

	name = StringField('Name')
	friend_code = StringField('Friend Code', [Length(min=9, max=9)])
	notes = TextAreaField('Notes', [Length(max=255)])
	visible = BooleanField('Visible', default=True)

	def validate_friend_code(form, field):
		if not field.data.isdigit():
			raise ValidationError('Field must be numeric.')
