
from flask.ext.security.forms import RegisterForm
from wtforms.fields import PasswordField
from wtforms.validators import EqualTo

# Because the developer of Flask-Security seriously thinks that
# having email confirmation is a reason to not have password confirmation.
# Fucking retard.
class RegisterFormWithAFuckingPasswordConfirmField(RegisterForm):
	password_confirm = PasswordField('Confirm Password', [EqualTo('password')])
