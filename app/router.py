
def routes(app):

	@app.all('/')
	def hello():
		return 'Hello World!'
