"""post table new column

Revision ID: 57a0e4ba1a21
Revises: 642a3a76dbef
Create Date: 2023-11-14 23:53:32.453897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57a0e4ba1a21'
down_revision = '642a3a76dbef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'updated_at')
    # ### end Alembic commands ###
