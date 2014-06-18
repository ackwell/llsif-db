
from flask import Flask, Blueprint
from app import router


# Extending to allow nicer routing interface
class Application(Flask):
	def route(self, rule, action=None, **kwargs):
		# Function that will either be called manually, or returned as a decorator
		def add_rule(func):
			self.add_url_rule(rule, func.__name__, func, **kwargs)

		# If action isn't None, it's likely being called as a function
		if action is None:
			return add_rule

		# TODO: Handle external controllers

	methods = [
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
		if name in self.methods:
			return get_wrapper([name.upper()])

		# Binding on all methods
		if name == 'all':
			return get_wrapper(self.methods)

		# Nothing found, pass to parent
		return getattr(super(Application, self), name)


if __name__ == '__main__':
	app = Application(__name__)

	# Load up the routes
	router.routes(app)

	# TODO: config option for debug, host, etc
	app.run(host='0.0.0.0', debug=True)
