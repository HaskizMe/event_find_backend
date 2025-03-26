from typing import List, Optional
from pydantic import BaseModel

class Event(BaseModel):
    id: int
    title: str
    address: str
    start_date: str
    end_date: str
    type: str
    description: str

class EventResponse(BaseModel):
    # count: int
    # next: Optional[str] = None
    # previous: Optional[str] = None
    results: List[Event]