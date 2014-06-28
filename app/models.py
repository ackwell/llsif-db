
from flask import current_app
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(current_app)


db.Model.metadata = db.MetaData(naming_convention={
	"ix": 'ix_%(column_0_label)s',
	"uq": "uq_%(table_name)s_%(column_0_name)s",
	"ck": "ck_%(table_name)s_%(constraint_name)s",
	"fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
	"pk": "pk_%(table_name)s"
})


# Card container
class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=False)
	name = db.Column(db.String(32))

	normal_state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
	normal_state = db.relationship('State',
		uselist=False,
		foreign_keys=[normal_state_id],
		lazy='joined',
		cascade='all, delete-orphan',
		single_parent=True)

	idolised_state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
	idolised_state = db.relationship('State',
		uselist=False,
		foreign_keys=[idolised_state_id],
		lazy='joined',
		cascade='all, delete-orphan',
		single_parent=True)

	attribute = db.Column(db.String(8))

	skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
	appeal_id = db.Column(db.Integer, db.ForeignKey('appeal.id'))

	availability = db.relationship('Region',
		secondary='availability',
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

	def __repr__(self):
		return self.name


# Card's centre skills
class Skill(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))

	cards = db.relationship('Card',
		backref='skill',
		lazy='dynamic')

	description = db.Column(db.Text)

	bonus_attribute = db.Column(db.String(8))
	scale_attribute = db.Column(db.String(8))
	scale = db.Column(db.Float)

	def __repr__(self):
		return self.name


# Card's appeal ability
class Appeal(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))

	cards = db.relationship('Card',
		backref='appeal',
		lazy='dynamic')

	description = db.Column(db.Text)

	award = db.Column(db.String(32))
	award_modifier = db.Column(db.Integer)

	proc_statistic = db.Column(db.String(16))
	proc_count = db.Column(db.Integer)
	proc_chance = db.Column(db.Float)

	def __repr__(self):
		return self.name


# Card <--> Region join table
availability = db.Table('availability',
	db.Column('card_id', db.Integer, db.ForeignKey('card.id'), primary_key=True),
	db.Column('region_id', db.String, db.ForeignKey('region.id'), primary_key=True)
)


# ohgodtheykeepreleasingnewregions
class Region(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String(32))

	def __repr__(self):
		return self.name
