"""add content column to posts table

Revision ID: 74d34690c131
Revises: 21c46ecf09a2
Create Date: 2024-09-04 20:01:57.738627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74d34690c131'
down_revision: Union[str, None] = '21c46ecf09a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
