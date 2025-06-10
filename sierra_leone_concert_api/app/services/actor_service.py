from sqlalchemy.orm import Session
from app import models, schemas

def get_all_actors(db: Session):
    return db.query(models.Actor).all()

def get_actor_by_id(actor_id: int, db: Session):
    return db.query(models.Actor).filter(models.Actor.id == actor_id).first()

def create_actor(actor: schemas.ActorCreate, db: Session):
    db_actor = models.Actor(
        name=actor.name,
        role=actor.role,
        play_id=actor.play_id
    )
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor

def update_actor(actor_id: int, actor: schemas.ActorCreate, db: Session):
    db_actor = get_actor_by_id(actor_id, db)
    if db_actor:
        db_actor.name = actor.name
        db_actor.role = actor.role
        db_actor.play_id = actor.play_id
        db.commit()
        db.refresh(db_actor)
    return db_actor

def delete_actor(actor_id: int, db: Session):
    db_actor = get_actor_by_id(actor_id, db)
    if db_actor:
        db.delete(db_actor)
        db.commit()
    return db_actor
