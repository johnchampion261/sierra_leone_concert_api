from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, database, services

router = APIRouter(prefix="/directors", tags=["Directors"])

@router.post("/", response_model=schemas.Director)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(database.get_db)):
    return services.director_service.create_director(db, director)

@router.get("/", response_model=List[schemas.Director])
def list_directors(db: Session = Depends(database.get_db)):
    return services.director_service.get_all_directors(db)

@router.get("/{director_id}", response_model=schemas.Director)
def get_director(director_id: int, db: Session = Depends(database.get_db)):
    return services.director_service.get_director(db, director_id)

@router.put("/{director_id}", response_model=schemas.Director)
def update_director(director_id: int, director: schemas.DirectorCreate, db: Session = Depends(database.get_db)):
    return services.director_service.update_director(db, director_id, director)

@router.delete("/{director_id}")
def delete_director(director_id: int, db: Session = Depends(database.get_db)):
    return services.director_service.delete_director(db, director_id)
