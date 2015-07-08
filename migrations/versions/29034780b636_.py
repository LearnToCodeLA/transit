"""empty message

Revision ID: 29034780b636
Revises: 1b73d1006fa8
Create Date: 2015-07-08 00:21:20.785660

"""

# revision identifiers, used by Alembic.
revision = '29034780b636'
down_revision = '1b73d1006fa8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['features.id'], ),
    sa.ForeignKeyConstraint(['photo_id'], ['photos.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('votes')
    op.add_column('features', sa.Column('photo_url', sa.String(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('features', 'photo_url')
    op.create_table('votes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('photo_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('feature_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], [u'features.id'], name=u'votes_feature_id_fkey'),
    sa.ForeignKeyConstraint(['photo_id'], [u'photos.id'], name=u'votes_photo_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], name=u'votes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'votes_pkey')
    )
    op.drop_table('classifications')
    ### end Alembic commands ###
