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

class EventsResponse(BaseModel):
    # count: int
    # next: Optional[str] = None
    # previous: Optional[str] = None
    results: List[Event]


class EventRequest(BaseModel):
    title: str
    address: str
    start_date: str
    end_date: str
    type: str
    description: str