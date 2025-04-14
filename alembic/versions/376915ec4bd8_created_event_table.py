"""created_event_table

Revision ID: 376915ec4bd8
Revises: 0925da52fed5
Create Date: 2025-04-12 16:41:21.845559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '376915ec4bd8'
down_revision: Union[str, None] = '0925da52fed5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('zip', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_attendees',
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('event_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_attendees')
    op.drop_table('events')
    # ### end Alembic commands ###
