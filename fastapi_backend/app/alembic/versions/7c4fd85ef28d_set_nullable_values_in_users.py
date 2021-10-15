"""Set nullable values in users

Revision ID: 7c4fd85ef28d
Revises: c099b1e75a78
Create Date: 2021-10-11 18:29:54.918950

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '7c4fd85ef28d'
down_revision = 'c099b1e75a78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
