"""create posts table

Revision ID: 3c39ceaf9f0f
Revises: 
Create Date: 2023-12-18 12:41:25.026551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c39ceaf9f0f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable= False, primary_key =True)
                            ,sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade(): 
    op.drop_table('posts')
    pass
