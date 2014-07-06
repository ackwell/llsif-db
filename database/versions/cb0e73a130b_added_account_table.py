"""Added account table

Revision ID: cb0e73a130b
Revises: 311939d34034
Create Date: 2014-07-06 04:44:19.285611

"""

# revision identifiers, used by Alembic.
revision = 'cb0e73a130b'
down_revision = '311939d34034'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('region_id', sa.String(length=8), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('friend_code', sa.String(length=16), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.Column('visible', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], name=op.f('fk_account_region_id_region')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_account_user_id_user')),
    sa.PrimaryKeyConstraint('user_id', 'region_id', name=op.f('pk_account'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    ### end Alembic commands ###
