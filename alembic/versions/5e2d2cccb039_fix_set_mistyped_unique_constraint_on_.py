"""fix: set mistyped unique constraint on ai_model instead of setting it on key

Revision ID: 5e2d2cccb039
Revises: b07431ff3758
Create Date: 2024-06-04 16:11:57.580087

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e2d2cccb039'
down_revision: Union[str, None] = 'b07431ff3758'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('api_keys_key_key', 'api_keys', type_='unique')
    op.create_unique_constraint(None, 'api_keys', ['ai_model'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'api_keys', type_='unique')
    op.create_unique_constraint('api_keys_key_key', 'api_keys', ['key'])
    # ### end Alembic commands ###
