"""Increase password_hashed column size

Revision ID: bd45621ecae1
Revises: 17871c418c09
Create Date: 2025-03-14 19:44:28.700065

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bd45621ecae1'
down_revision = '17871c418c09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hashed', sa.String(length=255), nullable=False))
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=False))
    op.drop_column('user', 'password_hashed')
    # ### end Alembic commands ###
