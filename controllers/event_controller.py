from fastapi import APIRouter, Depends

from schemas.event_schema import EventsResponse, Event, EventRequest
from services.event_service import EventService
from utils.auth_utility import get_current_user_id  # or wherever your function is


router = APIRouter(prefix="/api", tags=["Authorization"])

@router.get("/events", response_model=EventsResponse)
async def get_events():
    return await EventService.get_all_events()
    
# @router.post("/event", response_model=Event)
# async def create_event(event: EventRequest):
#     return await EventService.create_event(event)
@router.post("/event", response_model=Event)
async def create_event(
    event: EventRequest,
    user_id: int = Depends(get_current_user_id)
):
    return await EventService.create_event(event, user_id)  # ✅ Await the async method!