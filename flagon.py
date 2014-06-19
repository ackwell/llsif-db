
# Tiny bit of abstraction on top of Flask because hey why not

from flask import Flask
import importlib


# Flask wrapper
class Flagon(Flask):
	def __init__(self, *args, **kwargs):
		# Get settings from the kwargs
		self._app_module = kwargs.pop('app_module', 'app')

		# Set up Flask
		super(Flagon, self).__init__(*args, **kwargs)

		# Do other stuff
		self._initiate_routes()

	def _initiate_routes(self):
		router = importlib.import_module(self._app_module + '.router')
		router.routes(Router(self))


# Nicer routing interface
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
