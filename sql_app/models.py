from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Time,
    TIMESTAMP,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.ddl import CreateColumn
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from .database import Base


class Venue(Base):

    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    addressLine1 = Column(String)
    addressLine2 = Column(String)
    city = Column(String)
    postalCode = Column(String)
    email = Column(String)
    phone = Column(String)
    createdOn = Column(TIMESTAMP)

    events = relationship("Event", back_populates="owner")


class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    categoryId = Column(Integer, ForeignKey("category.id"))
    venueId = Column(Integer, ForeignKey("venues.id"))
    createdOn = Column(TIMESTAMP)

    owner = relationship("Venue", back_populates="events")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
