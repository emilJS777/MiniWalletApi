"""empty message

Revision ID: 47648638ea0a
Revises: 884cc2bc5abe
Create Date: 2025-01-11 16:22:14.886816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47648638ea0a'
down_revision = '884cc2bc5abe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallet_details', schema=None) as batch_op:
        batch_op.add_column(sa.Column('qr', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallet_details', schema=None) as batch_op:
        batch_op.drop_column('qr')

    # ### end Alembic commands ###
