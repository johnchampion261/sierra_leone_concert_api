from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, database, services

router = APIRouter(prefix="/plays", tags=["Plays"])

@router.post("/", response_model=schemas.Play)
def create_play(play: schemas.PlayCreate, db: Session = Depends(database.get_db)):
    return services.play_service.create_play(db, play)

@router.get("/", response_model=List[schemas.Play])
def get_plays(db: Session = Depends(database.get_db)):
    return services.play_service.get_all_plays(db)

@router.get("/{play_id}", response_model=schemas.Play)
def get_play(play_id: int, db: Session = Depends(database.get_db)):
    return services.play_service.get_play(db, play_id)

@router.put("/{play_id}", response_model=schemas.Play)
def update_play(play_id: int, play: schemas.PlayCreate, db: Session = Depends(database.get_db)):
    return services.play_service.update_play(db, play_id, play)

@router.delete("/{play_id}")
def delete_play(play_id: int, db: Session = Depends(database.get_db)):
    return services.play_service.delete_play(db, play_id)
