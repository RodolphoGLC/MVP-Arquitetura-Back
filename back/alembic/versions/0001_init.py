from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None

def upgrade():
    op.create_table(
        "teams",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100))
    )
    op.create_table(
        "team_pokemons",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("team_id", sa.Integer, sa.ForeignKey("teams.id")),
        sa.Column("pokemon_id", sa.Integer),
        sa.Column("name", sa.String(100)),
        sa.Column("image", sa.String(255))
    )

def downgrade():
    op.drop_table("team_pokemons")
    op.drop_table("teams")