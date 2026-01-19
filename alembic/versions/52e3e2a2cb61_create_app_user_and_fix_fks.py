"""create app_user and fix FKs

Revision ID: 52e3e2a2cb61
Revises: ab113b3ad8ad
Create Date: 2026-01-19 17:32:00.995108

"""
from typing import Sequence, Union
import sqlmodel

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52e3e2a2cb61'
down_revision: Union[str, Sequence[str], None] = 'ab113b3ad8ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
