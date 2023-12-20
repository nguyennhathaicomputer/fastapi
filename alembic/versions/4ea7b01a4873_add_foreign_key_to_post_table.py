"""add foreign-key to post table

Revision ID: 4ea7b01a4873
Revises: af7ddb64beb9
Create Date: 2023-12-18 14:35:42.499828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ea7b01a4873'
down_revision: Union[str, None] = 'af7ddb64beb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",referent_table = "users", 
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")    
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="post")
    op.drop_column('posts', 'owner_id')
    pass
