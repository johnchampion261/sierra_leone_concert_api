from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app import models

# Configuration
SECRET_KEY = "your-secret-key"  # Replace with a strong secret key (e.g., from environment variable)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ✅ Utility to verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# ✅ Utility to hash password
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# ✅ Authenticate user by email and password
def authenticate_user(email: str, password: str, db: Session):
    user = db.query(models.Customer).filter(models.Customer.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

# ✅ Create a JWT access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
