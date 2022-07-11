"""create schemas

Revision ID: 55700472d350
Revises: d24c62897ebb
Create Date: 2022-07-11 16:32:09.207460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55700472d350'
down_revision = 'd24c62897ebb'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("create schema schema_one")
    op.execute("create schema schema_two")


def downgrade():
    op.execute("drop schema schema_one")
    op.execute("drop schema schema_two")
