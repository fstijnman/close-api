from re import T
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
    DateTime,
    Float,
)
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.ddl import CreateColumn
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Date
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

    event = relationship("Event", back_populates="venue")
    openinghours = relationship("OpeningHoursVenue", back_populates="venue")
    venueprice = relationship("VenuePrice", back_populates="venue")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    categoryId = Column(Integer, ForeignKey("category.id"))
    priceId = Column(Integer, ForeignKey("eventprice.id"))
    venueId = Column(Integer, ForeignKey("venues.id"))
    createdOn = Column(TIMESTAMP)

    venue = relationship("Venue", back_populates="event")
    category = relationship("Category", back_populates="event")
    eventprice = relationship("EventPrice", back_populates="event")
    openinghours = relationship("OpeningHoursEvent", back_populates="event")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    event = relationship("Event", back_populates="category")


class VenuePrice(Base):
    __tablename__ = "venueprice"

    id = Column(Integer, primary_key=True, index=True)
    venueId = Column(Integer, ForeignKey("venue.Id"))
    priceRegular = Column(Float)
    priceStudent = Column(Float)
    priceAbove60 = Column(Float)
    priceUnder18 = Column(Float)
    priceCJP = Column(Float)
    priceMuseumCard = Column(Float)

    venue = relationship("Venue", back_populates="venueprice")


class EventPrice(Base):
    __tablename__ = "eventprice"

    id = Column(Integer, primary_key=True, index=True)
    eventId = Column(Integer, ForeignKey("event.Id"))
    priceRegular = Column(Float)
    priceStudent = Column(Float)
    priceAbove60 = Column(Float)
    priceUnder18 = Column(Float)
    priceCJP = Column(Float)
    priceMuseumCard = Column(Float)

    event = relationship("Event", back_populates="eventprice")


class OpeningHoursVenue(Base):
    __tablename__ = "openinghoursvenue"

    id = Column(Integer, primary_key=True, index=True)
    venueId = Column(Integer, ForeignKey("venues.id"))
    fromDate = Column(DateTime)
    toDate = Column(DateTime)
    weekDay = Column(Integer)
    startHour = Column(Integer)
    endHour = Column(Integer)

    venue = relationship("Venue", back_populates="openinghours")


class OpeningHoursEvent(Base):
    __tablename__ = "openinghoursvenue"

    id = Column(Integer, primary_key=True, index=True)
    eventId = Column(Integer, ForeignKey("events.id"))
    fromDate = Column(DateTime)
    toDate = Column(DateTime)
    weekDay = Column(Integer)
    startHour = Column(Integer)
    endHour = Column(Integer)

    event = relationship("Event", back_populates="openinghours")
