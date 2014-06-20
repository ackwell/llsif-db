
from app import app
from flagon import Router
route = Router(app)

route.all('/', 'hello')
