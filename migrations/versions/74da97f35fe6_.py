"""empty message

Revision ID: 74da97f35fe6
Revises: 57c1e823c528
Create Date: 2021-06-14 12:07:39.428495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74da97f35fe6'
down_revision = '57c1e823c528'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('choice', sa.Column('p1', sa.String(), nullable=True))
    op.add_column('choice', sa.Column('p2', sa.String(), nullable=True))
    op.add_column('choice', sa.Column('s1', sa.String(), nullable=True))
    op.add_column('choice', sa.Column('s2', sa.String(), nullable=True))
    op.add_column('choice', sa.Column('s3', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('choice', 's3')
    op.drop_column('choice', 's2')
    op.drop_column('choice', 's1')
    op.drop_column('choice', 'p2')
    op.drop_column('choice', 'p1')
    # ### end Alembic commands ###
