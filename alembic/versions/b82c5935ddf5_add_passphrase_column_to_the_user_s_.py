"""Add passphrase column to the user's model

Revision ID: b82c5935ddf5
Revises: 090f98593afb
Create Date: 2024-06-13 14:35:56.394360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b82c5935ddf5'
down_revision: Union[str, None] = '090f98593afb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('passphrase', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'passphrase')
    # ### end Alembic commands ###
