"""Add event table

Revision ID: f89c5e39d5c1
Revises: 
Create Date: 2019-05-23 04:53:34.502862

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'f89c5e39d5c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'event',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('price', postgresql.MONEY(), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('created_on', sa.DateTime(), nullable=False),
        sa.Column('modified_on', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_date'), 'event', ['date'], unique=False)
    op.create_index(op.f('ix_event_name'), 'event', ['name'], unique=False)

    conn = op.get_bind()
    date = str(datetime.now())
    conn.execute("""
    insert into event
        (name, date, price, created_on, modified_on)
            values
        (
            'Godsmack Concert',
            '09-25-2020',
            129.99,
            '{0}',
            '{0}'
        );
    """.format(date))


def downgrade():
    op.drop_index(op.f('ix_event_name'), table_name='event')
    op.drop_index(op.f('ix_event_date'), table_name='event')
    op.drop_table('event')
