from sqlalchemy.orm import Session
from app import models, schemas

def get_all_showtimes(db: Session):
    return db.query(models.ShowTime).all()

def get_showtime_by_id(showtime_id: int, db: Session):
    return db.query(models.ShowTime).filter(models.ShowTime.id == showtime_id).first()

def create_showtime(showtime: schemas.ShowTimeCreate, db: Session):
    db_showtime = models.ShowTime(**showtime.dict())
    db.add(db_showtime)
    db.commit()
    db.refresh(db_showtime)
    return db_showtime

def update_showtime(showtime_id: int, showtime: schemas.ShowTimeCreate, db: Session):
    db_showtime = get_showtime_by_id(showtime_id, db)
    if not db_showtime:
        return None
    for field, value in showtime.dict().items():
        setattr(db_showtime, field, value)
    db.commit()
    db.refresh(db_showtime)
    return db_showtime

def delete_showtime(showtime_id: int, db: Session):
    db_showtime = get_showtime_by_id(showtime_id, db)
    if not db_showtime:
        return None
    db.delete(db_showtime)
    db.commit()
    return db_showtime
