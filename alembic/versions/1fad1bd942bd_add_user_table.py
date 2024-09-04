"""add user table

Revision ID: 1fad1bd942bd
Revises: 74d34690c131
Create Date: 2024-09-04 20:08:29.791891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fad1bd942bd'
down_revision: Union[str, None] = '74d34690c131'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',sa.Column('id',sa.Integer(),nullable=False),
      sa.Column('email',sa.String(),nullable=False),
      sa.Column('password',sa.String(),nullable=False),
      sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
      sa.PrimaryKeyConstraint('id'),sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
