from app.database import Base, engine
from app import models  # ensure your models are imported so they get registered

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()
