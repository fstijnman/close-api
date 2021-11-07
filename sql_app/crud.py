from sqlalchemy.orm import Session

from . import models, schemas


def get_venue(db: Session, venue_id: int):
    return db.query(models.Venue).filter(models.Venue.id == venue_id).first()


def get_venue_by_name(db: Session, name: str):
    return db.query(models.Venue).filter(models.Venue.name == name).first()


def get_venues(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Venue).offset(skip).limit(limit).all()


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


def create_venue(db: Session, venue: schemas.VenueCreate):
    db_venue = models.Venue(**venue.dict())
    db.add(db_venue)
    db.commit()
    db.refresh(db_venue)
    return db_venue


def create_venue_event(db: Session, event: schemas.EventCreate, venue_id: int):
    db_event = models.Event(**event.dict(), venueId=venue_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
