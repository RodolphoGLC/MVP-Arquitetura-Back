from pydantic import BaseModel
from typing import List


class Pokemon(BaseModel):
    pokemon_id: int
    name: str
    image: str


class TeamCreate(BaseModel):
    name: str
    pokemons: List[Pokemon]


# 🔹 Para edição (PUT)
class TeamUpdate(BaseModel):
    name: str
    pokemons: List[Pokemon]


# 🔹 Para resposta (GET)
class TeamResponse(BaseModel):
    id: int
    name: str
    pokemons: List[Pokemon]

    class Config:
        orm_mode = True
