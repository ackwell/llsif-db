"""Remove attribute table

Revision ID: 4b81101e1101
Revises: 225b2aaf3a
Create Date: 2014-06-25 13:05:22.410154

"""

# revision identifiers, used by Alembic.
revision = '4b81101e1101'
down_revision = '225b2aaf3a'

from alembic import op
import sqlalchemy as sa

def upgrade():
    # Drop old skill columns
    # I spent way too long trying to get this shit working with alembic commands. Fuck it.
    op.execute('alter table `skill` drop foreign key `fk_skill_attribute_id_attribute`;')
    op.drop_column('skill', 'bonus')
    op.drop_column('skill', 'attribute_id')

    # New skill columns
    op.add_column('skill', sa.Column('bonus_attribute', sa.String(8), nullable=True))
    op.add_column('skill', sa.Column('scale_attribute', sa.String(8), nullable=True))
    op.add_column('skill', sa.Column('scale', sa.Float(), nullable=True))

    # Get rid of the Attribute table, it's kinda redundant
    op.execute('alter table `card` drop foreign key `fk_card_attribute_id_attribute`;')
    op.drop_column('card', 'attribute_id')
    op.drop_table('attribute')
    op.add_column('card', sa.Column('attribute', sa.String(8), nullable=True))


def downgrade():
    op.drop_column('skill', 'scale_attribute')
    op.drop_column('skill', 'scale')
    op.drop_column('skill', 'bonus_attribute')

    op.create_table('attribute',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=10), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.add_column('skill', sa.Column('attribute_id', sa.Integer(), sa.ForeignKey('attribute.id'), autoincrement=False, nullable=True))
    op.add_column('skill', sa.Column('bonus', sa.Integer(), autoincrement=False, nullable=True))
