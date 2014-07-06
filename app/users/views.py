
from flask import Blueprint, render_template
from flask.ext.security import current_user
from . import models

blueprint = Blueprint('accounts', __name__, url_prefix='/accounts')

@blueprint.route('/')
def index():
	accounts = models.Account.query.filter(
		(models.Account.visible == True) |
		(models.Account.user == current_user)
	).all()

	return render_template('accounts/index.html',
		accounts=accounts,
		current_user=current_user)
