from aiohttp import ClientSession

from app.api.dto.base import PageResponse, ApiResponse, PageRequest
from app.api.dto.user import UserResponse, LinkTelegramRequest
from app.api.route import UserRoute


class UserService:
    @staticmethod
    async def list_users() -> ApiResponse[PageResponse[UserResponse]]:
        async with ClientSession() as api:
            route = UserRoute.list_users()
            page = PageRequest(size=1_000_000).as_json()
            async with api.get(route, params=page) as response:
                return await PageResponse.parse(response, UserResponse)

    @staticmethod
    async def find_by_chat_id(chat_id: int) -> ApiResponse[UserResponse]:
        async with ClientSession() as api:
            route = UserRoute.find_by_chat_id(chat_id)
            async with api.get(route) as response:
                return await ApiResponse.parse(response, UserResponse)

    @staticmethod
    async def link_telegram(request: LinkTelegramRequest) -> ApiResponse:
        async with ClientSession() as api:
            route = UserRoute.link_telegram()
            async with api.post(route, json=request.as_json()) as response:
                return await ApiResponse.parse(response)
