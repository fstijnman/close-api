from re import T
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Float,
)
from sqlalchemy.sql import func
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
    priceId = Column(Integer, ForeignKey("venueprice.id"))
    createdOn = Column(DateTime(timezone=True), server_default=func.now())

    event = relationship("Event", back_populates="venue")
    category = relationship("CategoryVenue", back_populates="venue")
    openinghours = relationship("OpeningHoursVenue", back_populates="venue")
    venueprice = relationship("VenuePrice", back_populates="venue")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    priceId = Column(Integer, ForeignKey("eventprice.id"))
    venueId = Column(Integer, ForeignKey("venues.id"))
    createdOn = Column(DateTime(timezone=True), server_default=func.now())

    venue = relationship("Venue", back_populates="event")
    category = relationship("CategoryEvent", back_populates="event")
    eventprice = relationship("EventPrice", back_populates="event")
    openinghours = relationship("OpeningHoursEvent", back_populates="event")


class CategoryVenue(Base):
    __tablename__ = "categoryvenue"

    id = Column(Integer, primary_key=True, index=True)
    venueId = Column(Integer, ForeignKey("venues.id"))
    name = Column(String)

    venue = relationship("Venue", back_populates="category")


class CategoryEvent(Base):
    __tablename__ = "categoryevent"

    id = Column(Integer, primary_key=True, index=True)
    eventId = Column(Integer, ForeignKey("events.id"))
    name = Column(String)

    event = relationship("Event", back_populates="category")


class VenuePrice(Base):
    __tablename__ = "venueprice"

    id = Column(Integer, primary_key=True, index=True)
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
    __tablename__ = "openinghoursevent"

    id = Column(Integer, primary_key=True, index=True)
    eventId = Column(Integer, ForeignKey("events.id"))
    fromDate = Column(DateTime)
    toDate = Column(DateTime)
    weekDay = Column(Integer)
    startHour = Column(Integer)
    endHour = Column(Integer)

    event = relationship("Event", back_populates="openinghours")
