from sqlalchemy.orm import Session
from app import models, schemas

def get_all_plays(db: Session):
    return db.query(models.Play).all()

def get_play_by_id(play_id: int, db: Session):
    return db.query(models.Play).filter(models.Play.id == play_id).first()

def create_play(play: schemas.PlayCreate, db: Session):
    db_play = models.Play(**play.dict())
    db.add(db_play)
    db.commit()
    db.refresh(db_play)
    return db_play

def update_play(play_id: int, play: schemas.PlayCreate, db: Session):
    db_play = get_play_by_id(play_id, db)
    if db_play:
        for field, value in play.dict().items():
            setattr(db_play, field, value)
        db.commit()
        db.refresh(db_play)
    return db_play

def delete_play(play_id: int, db: Session):
    db_play = get_play_by_id(play_id, db)
    if db_play:
        db.delete(db_play)
        db.commit()
    return db_play
