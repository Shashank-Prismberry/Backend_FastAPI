"""Add content column

Revision ID: d571813b579a
Revises: 42f2ca04816b
Create Date: 2026-10-22 15:11:33.792693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd571813b579a'
down_revision: Union[str, Sequence[str], None] = '42f2ca04816b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
