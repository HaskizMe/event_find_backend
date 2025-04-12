


# class EventService:
#     @staticmethod
#     async def get_all_events() -> EventsResponse | None:
#         return EventRepository.EventRepository.get_all_events()
    
#     @staticmethod
#     async def get_event_by_id(event_id: int) -> Event | None:
#         try:
#             return EventRepository.EventRepository.get_event_by_id(event_id)
#         except FileNotFoundError:
#             raise HTTPException(status_code=500, detail="Events database file not found.")
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
#     @staticmethod
#     async def create_event(event, user_id: int) -> Event:
#         try:
#             # Pass both event and user_id to the repo layer
#             new_event = EventRepository.EventRepository.create_event(event, user_id)
#             if new_event is None:
#                 raise HTTPException(status_code=500, detail="Failed to create event.")
#             return new_event
#         except FileNotFoundError:
#             raise HTTPException(status_code=500, detail="Events database file not found.")
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
        

#     @staticmethod
#     async def set_attendance(event_id: int, user_id: int, attending: bool) -> Event:
#         try:
#             return EventRepository.EventRepository.setAttending(event_id, user_id, attending)
#         except FileNotFoundError:
#             raise HTTPException(status_code=500, detail="Events database file not found.")
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
        

#     @staticmethod
#     async def delete_event(event_id: int):
#         return EventRepository.EventRepository.delete_event(event_id)

from fastapi import HTTPException
from repositories.event_repository import EventRepository
from schemas.event_schema import EventsResponse, EventResponse, EventRequest


class EventService:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def get_all_events(self) -> EventsResponse:
        try:
            return self.event_repository.get_all_events()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving events: {str(e)}")

    async def get_event_by_id(self, event_id: int) -> EventResponse:
        try:
            event = self.event_repository.get_event_by_id(event_id)
            if not event:
                raise HTTPException(status_code=404, detail="Event not found")
            return event
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving event: {str(e)}")

    async def create_event(self, event: EventRequest, user_id: int) -> EventResponse:
        try:
            return self.event_repository.create_event(event, user_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating event: {str(e)}")

    async def set_attendance(self, event_id: int, user_id: int, attending: bool) -> EventResponse:
        try:
            return self.event_repository.set_attendance(event_id, user_id, attending)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error updating attendance: {str(e)}")

    async def delete_event(self, event_id: int):
        try:
            self.event_repository.delete_event(event_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting event: {str(e)}")