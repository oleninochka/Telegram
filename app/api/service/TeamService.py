from aiohttp import ClientSession

from app.api.dto.base import ApiResponse, PageResponse, PageRequest
from app.api.dto.team import TeamResponse, ParticipateRequest
from app.api.route import TeamRoute


class TeamService:
    @staticmethod
    async def list_teams() -> ApiResponse[PageResponse[TeamResponse]]:
        async with ClientSession() as api:
            route = TeamRoute.list_teams()
            page = PageRequest(size=1_000_000).as_json()
            async with api.get(route, params=page) as response:
                return await PageResponse.parse(response, TeamResponse)

    @staticmethod
    async def find_by_id(team_id: str) -> ApiResponse[TeamResponse]:
        async with ClientSession() as api:
            route = TeamRoute.find_by_id(team_id)
            async with api.get(route) as response:
                return await ApiResponse.parse(response, TeamResponse)

    @staticmethod
    async def participate(team_id: str, request: ParticipateRequest) -> ApiResponse:
        async with ClientSession() as api:
            route = TeamRoute.participate(team_id)
            async with api.post(route, json=request.as_json()) as response:
                return await ApiResponse.parse(response)
