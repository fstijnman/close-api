from typing import List, Optional

from pydantic import BaseModel


class EventBase(BaseModel):
    title: str
    description: str
    startDate: datetime
    endDate: datetime
