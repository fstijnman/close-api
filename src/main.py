from fastapi import FastAPI
from pydantic import BaseModel


class Venue(BaseModel):
    name: str
    description: Optional[str] = None
    city: str
    street: str
    number: str
    zip_code: str
    mobile: Optional[str]
    email: Optional[str]


app = FastAPI()


@app.post("/venues")
async def create_venue(venue: Venue):
    return venue
