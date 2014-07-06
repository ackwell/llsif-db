
from flask import Blueprint, render_template, abort, redirect, url_for
from flask.ext.security import current_user, login_required
from sqlalchemy.exc import IntegrityError
from . import models, forms
from ..extensions import db
from ..util import DeleteForm

blueprint = Blueprint('accounts', __name__, url_prefix='/accounts')

@blueprint.route('/')
def index():
	accounts = models.Account.query.filter(
		(models.Account.visible == True) |
		((models.Account.user == current_user) if current_user.is_authenticated() else False)
	).all()

	return render_template('accounts/index.html',
		accounts=accounts,
		current_user=current_user)


@blueprint.route('/create', methods=['GET', 'POST'], endpoint='create')
@blueprint.route('/edit/<int:user>/<region>', methods=['GET', 'POST'], endpoint='edit')
@login_required
def form(user=None, region=None):
	mode = 'new'

	account = None
	# Both user and region specified in url
	if user is not None and region is not None:
		# Trying to access page for another user, tell them to fuck off
		if user != current_user.id:
			return abort(403)

		# Usual query
		account = models.Account.query.get_or_404((user, region))
		mode = 'edit'

	# Only specified one of the two params, 404
	elif user is not None or region is not None:
		return abort(404)

	form = forms.Account(obj=account)

	if form.validate_on_submit():
		if account is None:
			account = models.Account()
		form.populate_obj(account)

		# Set the account's user to the current user
		account.user = current_user

		db.session.add(account)

		# Catch composite key dupes
		try:
			db.session.commit()
		except IntegrityError:
			form.region.errors.append('You already have an account saved for this region.')
			db.session.rollback()
		else:
			# Not logging - nobody but the user should be able to access it.
			return redirect(url_for('accounts.index'))

	return render_template('accounts/form.html',
		form=form,
		mode=mode)


@blueprint.route('/delete/<int:user>/<region>', methods=['POST'])
@login_required
def delete(user, region):
	if user != current_user.id:
		return abort(403)

	form = DeleteForm()

	if form.validate_on_submit():
		account = models.Account.query.get_or_404((user, region))
		db.session.delete(account)
		db.session.commit()

	return redirect(url_for('accounts.index'))
