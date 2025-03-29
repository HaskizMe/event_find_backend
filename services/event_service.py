from fastapi import HTTPException

import repositories.event_repository as EventRepository
from schemas.event_schema import EventsResponse


class EventService:
    @staticmethod
    async def get_all_events() -> EventsResponse | None:
        return EventRepository.EventRepository.get_all_events()
    
    @staticmethod
    async def create_event(event, user_id: int) -> EventsResponse:
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