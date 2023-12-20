"""add user table

Revision ID: af7ddb64beb9
Revises: 1af3ae453aa8
Create Date: 2023-12-18 14:07:24.771784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af7ddb64beb9'
down_revision: Union[str, None] = '1af3ae453aa8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable =False),
                    sa.Column('email', sa.String(), nullable =False),
                    sa.Column('password',sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
