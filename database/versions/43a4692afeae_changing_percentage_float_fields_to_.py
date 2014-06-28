"""Changing percentage float fields to integer

Revision ID: 43a4692afeae
Revises: 52fb43a5ba34
Create Date: 2014-06-28 04:03:12.835453

"""

# revision identifiers, used by Alembic.
revision = '43a4692afeae'
down_revision = '52fb43a5ba34'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('skill', 'scale', existing_type=sa.Float, type_=sa.Integer)
    op.alter_column('appeal', 'proc_chance', existing_type=sa.Float, type_=sa.Integer)


def downgrade():
    op.alter_column('skill', 'scale', existing_type=sa.Integer, type_=sa.Float)
    op.alter_column('appeal', 'proc_chance', existing_type=sa.Integer, type_=sa.Float)
