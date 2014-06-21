
from app import app
from flagon import Router
route = Router(app)

route.get('/', 'home.index')

# Cards
# TODO: I should probably add a namespacing/resource thingy to flagon.Router. Meh.
route.get('/cards', 'cards.index')
route.get('/cards/new', 'cards.new')
route.post('/cards/new', 'cards.new')
