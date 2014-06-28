
from setuptools import setup

setup(
	name='LoveLive: School Idol Festival - Database',
	version='0.1',
	packages=['app'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'Flask',
		'Flask-SQLAlchemy',
		'Flask-WTF',
		'MySQL-python'
	]
)
