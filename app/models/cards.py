
from app.models import db


# Card container
class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))

	normal_state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
	normal_state = db.relationship('State', uselist=False)

	idolised_state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
	idolised_state = db.relationship('State', uselist=False)

	attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'))
	attribute = db.relationship('Attribute', backref='cards', lazy='dynamic')

	skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
	skill = db.relationship('Skill', backref='cards', lazy='dynamic')

	appeal_id = db.Column(db.Integer, db.ForeignKey('appeal.id'))
	appeal = db.relationship('Appeal', backref='cards', lazy='dynamic')

	availability = db.relationship('Availability', backref='cards', lazy='dynamic')


# Card data that differs depending on idolised status
class State(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	rarity_id = db.Column(db.Integer, db.ForeignKey('rarity.id'))
	rarity = db.relationship('Rarity', backref='states', lazy='dynamic')

	icon = db.Column(db.String(64))
	image = db.Column(db.String(64))

	hp = db.Column(db.Integer)
	smile = db.Column(db.Integer)
	pure = db.Column(db.Integer)
	cool = db.Column(db.Integer)


# Data that is only dependant on the rarity
class Rarity(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))

	level = db.Column(db.Integer)
	bond = db.Column(db.Integer)


# Attribute of card (Smile / Pure / Cool)
class Attribute(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10))


# Card's centre skills
class Skill(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))

	description = db.Column(db.Text)

	attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'))
	attribute = db.relationship('Attribute', backref='cards', lazy='dynamic')

	bonus = db.Column(db.Integer)


# Card's appeal ability
class Appeal(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))

	description = db.Column(db.Text)

	type = db.Column(db.String(32))


# Availability of a card across the various regional versions
class Availability(db.Model):
	card_id = db.Column(db.Integer, db.ForeignKey('card.id'), primary_key=True)
	region = db.Column(db.String(10), primary_key=True)
