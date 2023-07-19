"""first migration

Revision ID: dc5f8713599d
Revises: 
Create Date: 2023-07-19 20:24:37.415203

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "dc5f8713599d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_items_description"), "items", ["description"], unique=False
    )
    op.create_index(op.f("ix_items_id"), "items", ["id"], unique=False)
    op.create_index(op.f("ix_items_title"), "items", ["title"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_items_title"), table_name="items")
    op.drop_index(op.f("ix_items_id"), table_name="items")
    op.drop_index(op.f("ix_items_description"), table_name="items")
    op.drop_table("items")
    # ### end Alembic commands ###
