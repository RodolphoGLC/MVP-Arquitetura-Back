from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.team import Team, TeamPokemon
from app.schemas.team import TeamCreate, TeamUpdate, TeamResponse

router = APIRouter(prefix="/teams", tags=["Teams"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ GET /teams
@router.get("/", response_model=list[TeamResponse])
def list_teams(db: Session = Depends(get_db)):
    return db.query(Team).all()


# ✅ GET /teams/{id}
@router.get("/{team_id}", response_model=TeamResponse)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = db.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


# ✅ POST /teams
@router.post("/", response_model=TeamResponse)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    t = Team(name=team.name)
    db.add(t)
    db.commit()
    db.refresh(t)

    for p in team.pokemons:
        db.add(TeamPokemon(team_id=t.id, **p.dict()))

    db.commit()
    db.refresh(t)
    return t


# ✅ PUT /teams/{id}
@router.put("/{team_id}", response_model=TeamResponse)
def update_team(team_id: int, data: TeamUpdate, db: Session = Depends(get_db)):
    team = db.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    # Atualiza nome
    team.name = data.name

    # Remove pokémons antigos
    db.query(TeamPokemon).filter(
        TeamPokemon.team_id == team_id
    ).delete()

    # Adiciona novos
    for p in data.pokemons:
        db.add(TeamPokemon(team_id=team_id, **p.dict()))

    db.commit()
    db.refresh(team)
    return team


# ✅ DELETE /teams/{id}
@router.delete("/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = db.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    db.delete(team)
    db.commit()
    return {"ok": True}
