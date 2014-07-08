
from flask.ext.assets import Bundle
from .extensions import assets

def register_assets():
	css = Bundle('css/*.css')

	less = Bundle('less/main.less',
		filters='less',
		output='.gen/less.css')

	all_css = Bundle(css, less,
		filters='cssmin',
		output='all.css')

	assets.register('css', all_css)
