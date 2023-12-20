""" add last few columns to posts table

Revision ID: 6a6416a912a5
Revises: 4ea7b01a4873
Create Date: 2023-12-18 14:47:37.847283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a6416a912a5'
down_revision: Union[str, None] = '4ea7b01a4873'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('published',sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable =False,server_default=sa.text('now()')))


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('post','created_at')
    pass
