from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, database, services

router = APIRouter(prefix="/actors", tags=["Actors"])

@router.post("/", response_model=schemas.Actor)
def create_actor(actor: schemas.ActorCreate, db: Session = Depends(database.get_db)):
    return services.actor_service.create_actor(db, actor)

@router.get("/", response_model=List[schemas.Actor])
def get_actors(db: Session = Depends(database.get_db)):
    return services.actor_service.get_all_actors(db)

@router.get("/{actor_id}", response_model=schemas.Actor)
def get_actor(actor_id: int, db: Session = Depends(database.get_db)):
    return services.actor_service.get_actor(db, actor_id)

@router.put("/{actor_id}", response_model=schemas.Actor)
def update_actor(actor_id: int, actor: schemas.ActorCreate, db: Session = Depends(database.get_db)):
    return services.actor_service.update_actor(db, actor_id, actor)

@router.delete("/{actor_id}")
def delete_actor(actor_id: int, db: Session = Depends(database.get_db)):
    return services.actor_service.delete_actor(db, actor_id)
