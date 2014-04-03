"""Clear out unneeded models and empty ballot measures

Revision ID: 13dd115bb2dc
Revises: 579070c00568
Create Date: 2014-04-02 20:24:59.751369

"""

# revision identifiers, used by Alembic.
revision = '13dd115bb2dc'
down_revision = '579070c00568'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import func

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contract', 'service_id')
    op.drop_table('service')
    ### end Alembic commands ###
    op.execute('''
        DELETE FROM stance WHERE ballot_measure_id IN (SELECT id FROM ballot_measure WHERE name IS NULL);
        DELETE FROM ballot_measure WHERE name IS NULL;
        ''')


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contract', sa.Column('service_id', postgresql.UUID(), nullable=True))
    op.create_table('service',
    sa.Column('id', postgresql.UUID(), server_default=func.uuid_generate_v4(), autoincrement=False, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=func.now(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=func.now(), autoincrement=False, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'service_pkey')
    )
    ### end Alembic commands ###