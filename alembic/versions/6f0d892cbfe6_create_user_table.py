"""create user table

Revision ID: 6f0d892cbfe6
Revises: 
Create Date: 2022-03-19 12:13:18.959906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f0d892cbfe6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('fullname', sa.Unicode(255), nullable=False),
                    sa.Column('email', sa.Unicode(255), nullable=True),
                    sa.Column('password', sa.String(255), nullable=False),
                    sa.Column('created_at', sa.DateTime, nullable=False, server_default='now()'),
                    sa.Column('updated_at', sa.DateTime, nullable=False, server_default='now()'),
                    )


def downgrade():
    op.drop_table('users')
