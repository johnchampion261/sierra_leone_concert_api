from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, database, services
from app.dependencies import get_current_user

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_model=schemas.Ticket)
def book_ticket(ticket: schemas.TicketCreate, db: Session = Depends(database.get_db), user=Depends(get_current_user)):
    return services.ticket_service.book_ticket(db, ticket, user)

@router.get("/", response_model=List[schemas.Ticket])
def get_tickets(db: Session = Depends(database.get_db)):
    return services.ticket_service.get_all_tickets(db)

@router.get("/{ticket_id}", response_model=schemas.Ticket)
def get_ticket(ticket_id: int, db: Session = Depends(database.get_db)):
    return services.ticket_service.get_ticket(db, ticket_id)
