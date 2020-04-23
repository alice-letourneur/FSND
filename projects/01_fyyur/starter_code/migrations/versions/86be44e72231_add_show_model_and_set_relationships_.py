"""Add Show model and set relationships: One artist can have many shows - One venue can have many shows

Revision ID: 86be44e72231
Revises: 66ce65fa5e3b
Create Date: 2020-04-23 19:29:49.525440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86be44e72231'
down_revision = '66ce65fa5e3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Show')
    # ### end Alembic commands ###
