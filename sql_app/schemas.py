from typing import List, Optional

from pydantic import BaseModel


class VenueBase(BaseModel):
    name: str
    description: Optional[str] = None
    addressLine1: str
    addressLine2: Optional[str] = None
    city: str
    postalCode: str
    email: Optional[str] = None
    phone: Optional[str] = None


class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    startDate: datetime
    endDate: datetime

class VenueCreate(VenueBase):
    pass

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    venueId: int

    class Config:
        orm_mode = True

class Venue(VenueBase):
    id: int
    events: List[Event]: []

    class Config:
        orm_mode = True
