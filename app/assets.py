
from flask.ext.assets import Bundle
from .extensions import assets

def register_assets():
	less = Bundle('less/main.less',
		filters='less',
		output='gen/less.css')

	css = Bundle('css/*.css',
		output='')

	all_css = Bundle(less, css,
		filters='cssmin',
		output='all.css')

	assets.register('css', all_css)
