from typing import List, Optional
from pydantic import BaseModel

class Event(BaseModel):
    id: int
    user_id: int
    title: str
    address: str
    start_date: str
    end_date: str
    type: str
    description: str
    attendees: List[int]

class EventsResponse(BaseModel):
    # count: int
    # next: Optional[str] = None
    # previous: Optional[str] = None
    results: List[Event]


# What the frontend sends
class EventRequest(BaseModel):
    title: str
    address: str
    start_date: str
    end_date: str
    type: str
    description: str

class AttendanceRequest(BaseModel):
    attending: bool