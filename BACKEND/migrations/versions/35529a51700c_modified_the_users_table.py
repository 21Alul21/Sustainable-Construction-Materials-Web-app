"""modified the Users table

Revision ID: 35529a51700c
Revises: 
Create Date: 2024-02-08 06:56:46.019702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35529a51700c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
