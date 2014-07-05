
from flask.ext.security import current_user

def context_processor():
	return {
		'logged_in': current_user.is_authenticated()
	}
