"""create posts table

Revision ID: 21c46ecf09a2
Revises: 
Create Date: 2024-09-04 19:42:38.792798

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision= '21c46ecf09a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
    sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
