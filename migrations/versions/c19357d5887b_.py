"""empty message

Revision ID: c19357d5887b
Revises: 9a5f6ed24083
Create Date: 2020-06-04 16:29:14.982073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c19357d5887b'
down_revision = '9a5f6ed24083'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article_user', sa.Column('email', sa.String(length=120), nullable=True))
    op.drop_constraint('article_user_email1_key', 'article_user', type_='unique')
    op.create_unique_constraint(None, 'article_user', ['email'])
    op.drop_column('article_user', 'email1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article_user', sa.Column('email1', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'article_user', type_='unique')
    op.create_unique_constraint('article_user_email1_key', 'article_user', ['email1'])
    op.drop_column('article_user', 'email')
    # ### end Alembic commands ###
