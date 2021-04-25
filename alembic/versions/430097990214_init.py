"""init

Revision ID: 430097990214
Revises: 
Create Date: 2021-04-24 22:28:42.484758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '430097990214'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Houses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('zip_code', sa.String, nullable=False),
        sa.Column('city', sa.String, nullable=False),
        sa.Column('neighborhood', sa.String, nullable=False),
        sa.Column('street', sa.String, nullable=False),
        sa.Column('number', sa.Integer),
        sa.Column('floor_quant', sa.Integer, nullable=False),
        sa.Column('rooms', sa.Integer),
        sa.Column('land_area', sa.Float, nullable=False),
        sa.Column('area', sa.Float, nullable=False),
        sa.Column('definition', sa.Boolean, nullable=False),
        sa.Column('price', sa.Float, nullable=False)
    )
    op.create_table(
        'Apartments',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('zip_code', sa.String, nullable=False),
        sa.Column('city', sa.String, nullable=False),
        sa.Column('neighborhood', sa.String, nullable=False),
        sa.Column('street', sa.String, nullable=False),
        sa.Column('number', sa.Integer),
        sa.Column('definition', sa.Boolean, nullable=False),
        sa.Column('area', sa.Float, nullable=False),
        sa.Column('condom_value', sa.Float, nullable=False),
        sa.Column('rooms', sa.Integer),
        sa.Column('floor', sa.Integer, nullable=False),
        sa.Column('garage_spots', sa.Integer),
        sa.Column('sun_position', sa.String),      
        sa.Column('price', sa.Float, nullable=False)
    )
    op.create_table(
        'Lands',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('zip_code', sa.String, nullable=False),
        sa.Column('city', sa.String, nullable=False),
        sa.Column('neighborhood', sa.String, nullable=False),
        sa.Column('street', sa.String, nullable=False),
        sa.Column('number', sa.Integer),
        sa.Column('definition', sa.Boolean, nullable=False),
        sa.Column('area', sa.Float, nullable=False),   
        sa.Column('price', sa.Float, nullable=False)
    )

def downgrade():
    op.drop_table('Houses')
    op.drop_table('Apartments')
    op.drop_table('Lands')