"""empty message

Revision ID: 9fc289c268a2
Revises: 8a7462da9e6c
Create Date: 2025-03-28 15:49:21.564365

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9fc289c268a2'
down_revision = '8a7462da9e6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('issue_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['issue_id'], ['issue.id'], name='comment_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='comment_ibfk_2', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
