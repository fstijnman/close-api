from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/venues/", response_model=schemas.Venue)
def create_venue(venue: schemas.VenueCreate, db: Session = Depends(get_db)):
    db_venue = crud.get_venue_by_name(db, name=venue.name)
    if db_venue:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_venue(db=db, venue=venue)


@app.get("/venues/", response_model=List[schemas.Venue])
def read_venues(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    venues = crud.get_venues(db, skip=skip, limit=limit)
    return venues


@app.get("/venues/{venue_id}", response_model=schemas.Venue)
def read_venue(venue_id: int, db: Session = Depends(get_db)):
    db_venue = crud.get_venue(db, venue_id=venue_id)
    if db_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return db_venue


@app.post("/venues/{venue_id}/events/", response_model=schemas.Event)
def create_event_for_venue(
    venue_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)
):
    return crud.create_venue_event(db=db, event=event, venue_id=venue_id)


@app.get("/events/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events
