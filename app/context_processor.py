
from flask.ext.security import current_user
from .util import DeleteForm

def context_processor():
	return {
		'logged_in': current_user.is_authenticated(),
		'delete_form': lambda: DeleteForm()
	}
