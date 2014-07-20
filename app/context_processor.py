
from flask import current_app, url_for
from flask.ext.security import current_user
from .util import DeleteForm

def context_processor():
	return {
		'logged_in': current_user.is_authenticated(),
		'delete_form': DeleteForm,
		'static_files': current_app.config['STATIC_FILE_BASE'] if 'STATIC_FILE_BASE' in current_app.config else url_for('static', filename='')
	}
