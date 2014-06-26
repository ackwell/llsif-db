"""Proper schema for Appeal table

Revision ID: 52fb43a5ba34
Revises: 4b81101e1101
Create Date: 2014-06-26 14:02:40.841263

"""

# revision identifiers, used by Alembic.
revision = '52fb43a5ba34'
down_revision = '4b81101e1101'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('appeal', 'type', new_column_name='award', existing_type=sa.String(32))
    op.add_column('appeal', sa.Column('award_modifier', sa.Integer()))
    op.add_column('appeal', sa.Column('proc_statistic', sa.String(16)))
    op.add_column('appeal', sa.Column('proc_count', sa.Integer()))
    op.add_column('appeal', sa.Column('proc_chance', sa.Float()))


def downgrade():
    op.alter_column('appeal', 'award', new_column_name='type', existing_type=sa.String(32))
    op.drop_column('appeal', 'award_modifier')
    op.drop_column('appeal', 'proc_statistic')
    op.drop_column('appeal', 'proc_count')
    op.drop_column('appeal', 'proc_chance')
