from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base


class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # One director can have many plays
    plays = relationship("Play", back_populates="director", cascade="all, delete")


class Play(Base):
    __tablename__ = "plays"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    duration = Column(Integer, nullable=True)
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=False)

    director = relationship("Director", back_populates="plays")
    showtimes = relationship("ShowTime", back_populates="play", cascade="all, delete")

    # Optional: if you want to access actors from a play
    actors = relationship("Actor", back_populates="play", cascade="all, delete")


class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=True)
    play_id = Column(Integer, ForeignKey("plays.id"), nullable=False)

    # Relationship back to Play for easy querying
    play = relationship("Play", back_populates="actors")


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)  # Store hashed password, never plain text

    # One customer can have many tickets
    tickets = relationship("Ticket", back_populates="customer", cascade="all, delete")


class ShowTime(Base):
    __tablename__ = "showtimes"
    id = Column(Integer, primary_key=True, index=True)
    play_id = Column(Integer, ForeignKey("plays.id"), nullable=False)
    date = Column(DateTime, nullable=False)

    play = relationship("Play", back_populates="showtimes")
    tickets = relationship("Ticket", back_populates="showtime", cascade="all, delete")


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    showtime_id = Column(Integer, ForeignKey("showtimes.id"), nullable=False)
    seat = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    showtime = relationship("ShowTime", back_populates="tickets")
    customer = relationship("Customer", back_populates="tickets")
