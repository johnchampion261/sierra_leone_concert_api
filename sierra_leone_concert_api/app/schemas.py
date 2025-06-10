from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# --- Director Schemas ---
class DirectorBase(BaseModel):
    name: str

class DirectorCreate(DirectorBase):
    pass

class Director(DirectorBase):
    id: int
    plays: List["Play"] = []

    class Config:
        orm_mode = True

# --- Play Schemas ---
class PlayBase(BaseModel):
    title: str
    genre: Optional[str] = None
    duration: Optional[int] = None
    director_id: int

class PlayCreate(PlayBase):
    pass

class Play(PlayBase):
    id: int
    director: Director
    showtimes: List["ShowTime"] = []

    class Config:
        orm_mode = True

# --- Actor Schemas ---
class ActorBase(BaseModel):
    name: str
    role: Optional[str] = None
    play_id: int

class ActorCreate(ActorBase):
    pass

class Actor(ActorBase):
    id: int

    class Config:
        orm_mode = True

# --- Customer Schemas ---
class CustomerBase(BaseModel):
    name: str
    email: EmailStr

class CustomerCreate(CustomerBase):
    password: str  # plaintext password input for creation

class Customer(CustomerBase):
    id: int
    # optionally include tickets if needed: tickets: List["Ticket"] = []

    class Config:
        orm_mode = True

# --- ShowTime Schemas ---
class ShowTimeBase(BaseModel):
    play_id: int
    date: datetime

class ShowTimeCreate(ShowTimeBase):
    pass

class ShowTime(ShowTimeBase):
    id: int

    class Config:
        orm_mode = True

# --- Ticket Schemas ---
class TicketBase(BaseModel):
    customer_id: int
    showtime_id: int
    seat: str
    price: float

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode = True


# --- Auth Token Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None


# To allow forward references (e.g., Play refers to Director and ShowTime)
Play.update_forward_refs()
Director.update_forward_refs()
ShowTime.update_forward_refs()
