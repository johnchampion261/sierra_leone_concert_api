from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, database, services

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(database.get_db)):
    return services.customer_service.create_customer(db, customer)

@router.get("/", response_model=List[schemas.Customer])
def get_customers(db: Session = Depends(database.get_db)):
    return services.customer_service.get_all_customers(db)

@router.get("/{customer_id}", response_model=schemas.Customer)
def get_customer(customer_id: int, db: Session = Depends(database.get_db)):
    return services.customer_service.get_customer(db, customer_id)

@router.put("/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, customer: schemas.CustomerCreate, db: Session = Depends(database.get_db)):
    return services.customer_service.update_customer(db, customer_id, customer)

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(database.get_db)):
    return services.customer_service.delete_customer(db, customer_id)
