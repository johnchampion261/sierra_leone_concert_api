from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Get all customers
def get_all_customers(db: Session):
    return db.query(models.Customer).all()

# Get customer by ID
def get_customer_by_id(customer_id: int, db: Session):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

# Get customer by email
def get_customer_by_email(email: str, db: Session):
    return db.query(models.Customer).filter(models.Customer.email == email).first()

# Create a new customer
def create_customer(customer: schemas.CustomerCreate, db: Session):
    hashed_password = pwd_context.hash(customer.password)
    db_customer = models.Customer(
        name=customer.name,
        email=customer.email,
        hashed_password=hashed_password  # ✅ FIXED: match your model field
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# Update existing customer
def update_customer(customer_id: int, customer: schemas.CustomerCreate, db: Session):
    db_customer = get_customer_by_id(customer_id, db)
    if db_customer:
        update_data = customer.dict()
        if "password" in update_data:
            update_data["hashed_password"] = pwd_context.hash(update_data.pop("password"))  # ✅ FIXED
        for field, value in update_data.items():
            setattr(db_customer, field, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer

# Delete a customer
def delete_customer(customer_id: int, db: Session):
    db_customer = get_customer_by_id(customer_id, db)
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer
