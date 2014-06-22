
from app import app
from flagon import Router
route = Router(app)

route.get('/', 'home.index')

# Cards
# TODO: I should probably add a namespacing/resource thingy to flagon.Router. Meh.
route.get('/cards', 'cards.index')
route.get('/cards/create', 'cards.create')
route.post('/cards/create', 'cards.create')
