#!venv/bin/python
from app import create_app
create_app().run(host='0.0.0.0', debug=True)