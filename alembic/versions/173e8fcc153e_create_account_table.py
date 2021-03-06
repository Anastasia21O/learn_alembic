"""create account table

Revision ID: 173e8fcc153e
Revises: 
Create Date: 2022-07-07 14:19:16.424976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '173e8fcc153e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')
