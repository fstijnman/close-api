from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Venue(Base):

    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    street = Column(String, unique=True, index=True)
    street_number = Column(String, unique=True, index=True)
    city = Column(String, unique=True, index=True)
    zip_code = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)

    events = relationship("Event", back_populates="owner")


class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    date_from = Column(String, index=True)
    date_to = Column(String, index=True)
    category = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("venues.id"))

    owner = relationship("Venue", back_populates="events")
