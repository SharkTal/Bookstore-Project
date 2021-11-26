"""add order_id and completed columns for orders

Revision ID: 70b261a44437
Revises: 34d74e1e4773
Create Date: 2021-11-26 14:10:55.773972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70b261a44437'
down_revision = '34d74e1e4773'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('order_id', sa.String(), nullable=True))
    op.add_column('orders', sa.Column('completed', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_orders_completed'), 'orders', ['completed'], unique=False)
    op.create_index(op.f('ix_orders_order_id'), 'orders', ['order_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_order_id'), table_name='orders')
    op.drop_index(op.f('ix_orders_completed'), table_name='orders')
    op.drop_column('orders', 'completed')
    op.drop_column('orders', 'order_id')
    # ### end Alembic commands ###
