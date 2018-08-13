"""empty message

Revision ID: 8f613cc2ce7b
Revises: 0813c0d2d836
Create Date: 2018-08-02 23:10:00.364519

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8f613cc2ce7b'
down_revision = '0813c0d2d836'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tokenuserd', sa.Column('token', sa.String(length=150), nullable=True))
    op.create_index(op.f('ix_tokenuserd_token'), 'tokenuserd', ['token'], unique=False)
    op.drop_index('ix_tokenuserd_toekn', table_name='tokenuserd')
    op.drop_column('tokenuserd', 'toekn')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tokenuserd', sa.Column('toekn', mysql.VARCHAR(length=150), nullable=True))
    op.create_index('ix_tokenuserd_toekn', 'tokenuserd', ['toekn'], unique=False)
    op.drop_index(op.f('ix_tokenuserd_token'), table_name='tokenuserd')
    op.drop_column('tokenuserd', 'token')
    # ### end Alembic commands ###