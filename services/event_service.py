import repositories.event_repository as EventRepository
from schemas.event_schema import EventResponse


class SWAPIService:
    @staticmethod
    async def get_all_events() -> EventResponse | None:
        return EventRepository