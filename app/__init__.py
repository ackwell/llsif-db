
from flask import Flask, request

app = Flask(__name__)
app.config.from_object('app.config')

@app.context_processor
def context_processor():
	context = {}

	# Add an `ajax` var, true when page is requested with `ajax` field in GET or POST
	context['ajax'] = False
	if request.form.get('ajax', False) or request.args.get('ajax', False):
		context['ajax'] = True

	return context

from . import controllers, models
