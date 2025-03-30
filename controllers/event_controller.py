from fastapi import APIRouter, Depends, HTTPException

from schemas.event_schema import EventsResponse, Event, EventRequest, AttendanceRequest
from services.event_service import EventService
from utils.auth_utility import get_current_user_id 


router = APIRouter(prefix="/api", tags=["Authorization"])

@router.get("/events", response_model=EventsResponse)
async def get_events():
    return await EventService.get_all_events()

@router.post("/event", response_model=Event)
async def create_event(event: EventRequest, user_id: int = Depends(get_current_user_id)):
    return await EventService.create_event(event, user_id)


@router.post("/event/{event_id}/attend")
async def set_attendance(
    event_id: int,
    data: AttendanceRequest,
    user_id: int = Depends(get_current_user_id)
):
    return await EventService.set_attendance(event_id, user_id, data.attending)

# New endpoint to get a single event by ID
@router.get("/event/{event_id}", response_model=Event)
async def get_event(event_id: int):
    try:
        event = await EventService.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.delete("/event/{event_id}")
async def delete_event(event_id: int, user_id: int = Depends(get_current_user_id)):
    try:
        event = await EventService.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        if event.user_id != user_id:
            raise HTTPException(status_code=403, detail="You do not have permission to delete this event")
        await EventService.delete_event(event_id)
        return {"message": "Event deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))