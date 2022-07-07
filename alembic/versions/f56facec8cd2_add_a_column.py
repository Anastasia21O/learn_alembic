"""Add a column

Revision ID: f56facec8cd2
Revises: 173e8fcc153e
Create Date: 2022-07-07 14:53:30.851157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f56facec8cd2'
down_revision = '173e8fcc153e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
