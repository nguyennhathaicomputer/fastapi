"""add content column to posts tabel

Revision ID: 1af3ae453aa8
Revises: 3c39ceaf9f0f
Create Date: 2023-12-18 13:46:42.015903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1af3ae453aa8'
down_revision: Union[str, None] = '3c39ceaf9f0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable =False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
