"""Switching datatype of appeal effect modifier to float

Revision ID: 9fd0a19e215
Revises: 43a4692afeae
Create Date: 2014-06-29 03:24:29.935884

"""

# revision identifiers, used by Alembic.
revision = '9fd0a19e215'
down_revision = '43a4692afeae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('appeal', 'effect_modifier', existing_type=sa.Integer, type_=sa.Float)


def downgrade():
    op.alter_column('appeal', 'effect_modifier', existing_type=sa.Float, type_=sa.Integer)
