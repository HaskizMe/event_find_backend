from fastapi import HTTPException

import repositories.event_repository as EventRepository
from schemas.event_schema import EventsResponse, Event


class EventService:
    @staticmethod
    async def get_all_events() -> EventsResponse | None:
        return EventRepository.EventRepository.get_all_events()
    
    @staticmethod
    async def get_event_by_id(event_id: int) -> Event | None:
        try:
            return EventRepository.EventRepository.get_event_by_id(event_id)
        except FileNotFoundError:
            raise HTTPException(status_code=500, detail="Events database file not found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
    @staticmethod
    async def create_event(event, user_id: int) -> Event:
        try:
            # Pass both event and user_id to the repo layer
            new_event = EventRepository.EventRepository.create_event(event, user_id)
            if new_event is None:
                raise HTTPException(status_code=500, detail="Failed to create event.")
            return new_event
        except FileNotFoundError:
            raise HTTPException(status_code=500, detail="Events database file not found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
        

    @staticmethod
    async def set_attendance(event_id: int, user_id: int, attending: bool) -> Event:
        try:
            return EventRepository.EventRepository.setAttending(event_id, user_id, attending)
        except FileNotFoundError:
            raise HTTPException(status_code=500, detail="Events database file not found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")