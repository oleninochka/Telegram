from aiohttp import ClientSession

from app.api.dto.base import ApiResponse, ListResponse
from app.api.dto.event import EventResponse
from app.api.route import EventRoute


class EventService:
    @staticmethod
    async def list_events() -> ApiResponse[ListResponse[EventResponse]]:
        async with ClientSession() as api:
            route = EventRoute.list_events()
            async with api.get(route) as response:
                return await ListResponse.parse(response, EventResponse)

    @staticmethod
    async def find_by_id(event_id: str) -> ApiResponse[EventResponse]:
        async with ClientSession() as api:
            route = EventRoute.find_by_id(event_id)
            async with api.get(route) as response:
                return await ApiResponse.parse(response, EventResponse)
