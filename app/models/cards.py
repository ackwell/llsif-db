
from app.models import db


# Card container
class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=False)
	name = db.Column(db.String(32))

	normal_state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
	normal_state = db.relationship('State',
		uselist=False,
		foreign_keys=[normal_state_id],
		lazy='joined')

	idolised_state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
	idolised_state = db.relationship('State',
		uselist=False,
		foreign_keys=[idolised_state_id],
		lazy='joined')

	attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'))

	skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
	appeal_id = db.Column(db.Integer, db.ForeignKey('appeal.id'))

	availability = db.relationship('Availability',
		backref='cards',
		lazy='dynamic')


# Card data that differs depending on idolised status
class State(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	rarity_id = db.Column(db.Integer, db.ForeignKey('rarity.id'))

	icon = db.Column(db.String(256))
	image = db.Column(db.String(256))

	hp = db.Column(db.Integer)
	smile = db.Column(db.Integer)
	pure = db.Column(db.Integer)
	cool = db.Column(db.Integer)


# Data that is only dependant on the rarity
class Rarity(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=False)
	name = db.Column(db.String(20))

	states = db.relationship('State',
		backref='rarity',
		lazy='dynamic')

	level = db.Column(db.Integer)
	bond = db.Column(db.Integer)


# Attribute of card (Smile / Pure / Cool)
class Attribute(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10))

	cards = db.relationship('Card',
		backref=db.backref('attribute', lazy='joined'),
		lazy='dynamic')

	skills = db.relationship('Skill',
		backref='attribute',
		lazy='dynamic')


# Card's centre skills
class Skill(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))

	cards = db.relationship('Card',
		backref=db.backref('skill', lazy='joined'),
		lazy='dynamic')

	description = db.Column(db.Text)

	attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'))
	bonus = db.Column(db.Integer)


# Card's appeal ability
class Appeal(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))

	cards = db.relationship('Card',
		backref=db.backref('appeal', lazy='joined'),
		lazy='dynamic')

	description = db.Column(db.Text)

	type = db.Column(db.String(32))


# Availability of a card across the various regional versions
class Availability(db.Model):
	card_id = db.Column(db.Integer, db.ForeignKey('card.id'), primary_key=True)
	region = db.Column(db.String(10), primary_key=True)
