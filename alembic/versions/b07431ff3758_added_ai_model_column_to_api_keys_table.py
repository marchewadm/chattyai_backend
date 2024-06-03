"""Added ai_model column to api_keys table

Revision ID: b07431ff3758
Revises: 300ec423ec7a
Create Date: 2024-05-28 16:10:45.672475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b07431ff3758'
down_revision: Union[str, None] = '300ec423ec7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_keys', sa.Column('ai_model', sa.String(length=15), nullable=False))
    op.create_unique_constraint(None, 'api_keys', ['ai_model', 'user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'api_keys', type_='unique')
    op.drop_column('api_keys', 'ai_model')
    # ### end Alembic commands ###