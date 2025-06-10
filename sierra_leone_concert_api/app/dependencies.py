from fastapi import Depends
from sqlalchemy.orm import Session
from .database import get_db
from .auth import get_current_user
from . import models  # ✅ Import your DB models

# Dependency to get a DB session
def get_db_session(db: Session = Depends(get_db)) -> Session:
    return db

# Dependency to ensure authentication
def require_auth(current_user: models.Customer = Depends(get_current_user)) -> models.Customer:
    return current_user
