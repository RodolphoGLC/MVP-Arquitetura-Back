from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    pokemons = relationship("TeamPokemon", cascade="all, delete")

class TeamPokemon(Base):
    __tablename__ = "team_pokemons"
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    pokemon_id = Column(Integer)
    name = Column(String(100))
    image = Column(String(255))