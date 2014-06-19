
from flask import Flask, Blueprint
from app import router
import importlib


# Nicer routing interface, passed to router.routes
class Router(object):
	def __init__(self, app):
		self.app = app

	def route(self, rule, action=None, **kwargs):
		# Function that will either be called manually, or returned as a decorator
		def add_rule(func):
			name = kwargs.pop('name', None)
			self.app.add_url_rule(rule, name, func, **kwargs)

		# If action is none, the function is likely being used as a decorator
		if action is None:
			return add_rule

		func = self._get_view_function(action)
		add_rule(func)

	def _get_view_function(self, action):
		# TODO: Possibly handle more action formats
		controller, func = action.split('.') if '.' in action else ('app', action,)
		
		# TODO: Error handling
		# TODO: Config for controller directory
		# TODO: Possible support for controller classes
		module = importlib.import_module('app.controllers.' + controller)
		return getattr(module, func)

	_methods = [
		'get',
		'post',
		'put',
		'delete'
	]

	def __getattr__(self, name):
		def get_wrapper(methods):
			def wrapper(*args, **kwargs):
				return self.route(*args, methods=methods, **kwargs)
			return wrapper

		# They specified a specific http method
		if name in self._methods:
			return get_wrapper([name.upper()])

		# Binding on all methods
		if name == 'all':
			return get_wrapper(self._methods)

		# Nothing found, pass to parent
		return getattr(super(Application, self), name)


if __name__ == '__main__':
	app = Flask(__name__)

	# Load up the routes
	router.routes(Router(app))

	# TODO: config option for debug, host, etc
	app.run(host='0.0.0.0', debug=True)
