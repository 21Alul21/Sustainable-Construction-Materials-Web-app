"""modified Users table schema

Revision ID: 4ff845ea0852
Revises: 35529a51700c
Create Date: 2024-02-08 07:04:49.924324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ff845ea0852'
down_revision = '35529a51700c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('first_name')
        batch_op.drop_column('interest')
        batch_op.drop_column('last_name')
        batch_op.drop_column('is_active')
        batch_op.drop_column('discipline')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('discipline', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.VARCHAR(length=10), nullable=False))
        batch_op.add_column(sa.Column('interest', sa.TEXT(), nullable=False))
        batch_op.add_column(sa.Column('first_name', sa.VARCHAR(length=10), nullable=False))

    # ### end Alembic commands ###