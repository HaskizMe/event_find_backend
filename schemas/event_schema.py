from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class EventResponse(BaseModel):
    id: int
    user_id: int
    title: str
    address: str
    city: str
    state: str
    zip: str
    country: str
    start_date: date  # This allows auto-parsing from string
    type: str
    description: Optional[str] = None
    attendees: List[int] = []  # default to empty list

    class Config:
        from_attributes = True  # <- This is essential for converting from SQLAlchemy model

class EventsResponse(BaseModel):
    # count: int
    # next: Optional[str] = None
    # previous: Optional[str] = None
    results: List[EventResponse]


# What the frontend sends
class EventRequest(BaseModel):
    title: str
    address: str
    city: str
    state: str
    zip: str
    country: str
    start_date: str
    type: str
    description: str


class AttendanceRequest(BaseModel):
    attending: bool