"""add SpecialFishes table

迁移 ID: f70bdeaec7a4
父迁移: 68463f3e5f33
创建时间: 2024-04-11 12:59:25.138990

"""
from __future__ import annotations

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = 'f70bdeaec7a4'
down_revision: str | Sequence[str] | None = '68463f3e5f33'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nonebot_plugin_fishing_specialfishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=32), nullable=False),
    sa.Column('fish', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_nonebot_plugin_fishing_specialfishes')),
    info={'bind_key': 'nonebot_plugin_fishing'}
    )
    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nonebot_plugin_fishing_specialfishes')
    # ### end Alembic commands ###
