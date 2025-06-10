from sqlalchemy.orm import Session
from app import models, schemas

def get_all_directors(db: Session):
    return db.query(models.Director).all()

def get_director_by_id(director_id: int, db: Session):
    return db.query(models.Director).filter(models.Director.id == director_id).first()

def create_director(director: schemas.DirectorCreate, db: Session):
    db_director = models.Director(**director.dict())
    db.add(db_director)
    db.commit()
    db.refresh(db_director)
    return db_director

def update_director(director_id: int, director: schemas.DirectorCreate, db: Session):
    db_director = get_director_by_id(director_id, db)
    if db_director:
        for field, value in director.dict().items():
            setattr(db_director, field, value)
        db.commit()
        db.refresh(db_director)
    return db_director

def delete_director(director_id: int, db: Session):
    db_director = get_director_by_id(director_id, db)
    if db_director:
        db.delete(db_director)
        db.commit()
    return db_director
