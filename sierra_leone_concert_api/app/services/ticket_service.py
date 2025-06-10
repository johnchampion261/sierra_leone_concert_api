from sqlalchemy.orm import Session
from app import models, schemas

def get_all_tickets(db: Session):
    return db.query(models.Ticket).all()

def get_ticket_by_id(ticket_id: int, db: Session):
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

def create_ticket(ticket: schemas.TicketCreate, db: Session):
    db_ticket = models.Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def delete_ticket(ticket_id: int, db: Session):
    db_ticket = get_ticket_by_id(ticket_id, db)
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    return db_ticket
