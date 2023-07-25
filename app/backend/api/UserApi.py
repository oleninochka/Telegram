from dataclasses import asdict

from aiohttp import ClientSession

from app.backend.dto.base import ApiResponse, PageResponse
from app.backend.dto.user import UserResponse, LinkTelegramRequest
from app.config.ApiRoute import UserRoute


class UserApi:
    @staticmethod
    async def list_users() -> ApiResponse[PageResponse[UserResponse]]:
        async with ClientSession() as api:
            route = UserRoute.list_users()
            async with api.get(route) as response:
                return await ApiResponse.parse_page(UserResponse, response)

    @staticmethod
    async def find_by_chat_id(chat_id: int) -> ApiResponse[UserResponse]:
        async with ClientSession() as api:
            route = UserRoute.find_by_chat_id(chat_id)
            async with api.get(route) as response:
                return await ApiResponse.parse(UserResponse, response)

    @staticmethod
    async def link_telegram(request: LinkTelegramRequest) -> ApiResponse:
        async with ClientSession() as api:
            route = UserRoute.link_telegram()
            async with api.post(route, json=asdict(request)) as response:
                return await ApiResponse.parse_message(response)
