from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/showtimes", tags=["Showtimes"])

@router.post("/", response_model=schemas.ShowTime)
def create_showtime(showtime: schemas.ShowTimeCreate, db: Session = Depends(get_db)):
    db_showtime = models.ShowTime(**showtime.dict())
    db.add(db_showtime)
    db.commit()
    db.refresh(db_showtime)
    return db_showtime

@router.get("/", response_model=List[schemas.ShowTime])
def get_all_showtimes(db: Session = Depends(get_db)):
    return db.query(models.ShowTime).all()

@router.get("/{showtime_id}", response_model=schemas.ShowTime)
def get_showtime(showtime_id: int, db: Session = Depends(get_db)):
    showtime = db.query(models.ShowTime).filter(models.ShowTime.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return showtime

@router.delete("/{showtime_id}")
def delete_showtime(showtime_id: int, db: Session = Depends(get_db)):
    showtime = db.query(models.ShowTime).filter(models.ShowTime.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    db.delete(showtime)
    db.commit()
    return {"detail": "Showtime deleted"}
