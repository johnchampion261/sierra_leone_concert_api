from app.database import SessionLocal
from app.models import Customer
from app.auth import get_password_hash

def create_dwight_user():
    db = SessionLocal()
    try:
        email = "dwight@example.com"
        password = "1234"

        existing_user = db.query(Customer).filter(Customer.email == email).first()
        if existing_user:
            print("User already exists.")
            return

        hashed_password = get_password_hash(password)
        new_user = Customer(name="Dwight", email=email, hashed_password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        print(f"User '{email}' created successfully.")
    finally:
        db.close()

if __name__ == "__main__":
    create_dwight_user()
