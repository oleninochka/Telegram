from aiohttp import ClientSession

from app.api.dto.base import ApiResponse, PageResponse
from app.api.dto.score import ProfileScoreResponse, UserScoreResponse, TeamScoreResponse
from app.api.route import ScoreRoute


class ScoreService:
    @staticmethod
    async def profile_score(user_id: str) -> ApiResponse[ProfileScoreResponse]:
        async with ClientSession() as api:
            route = ScoreRoute.profile_score(user_id)
            async with api.get(route) as response:
                return await ApiResponse.parse(response, ProfileScoreResponse)

    @staticmethod
    async def user_scoreboard() -> ApiResponse[PageResponse[UserScoreResponse]]:
        async with ClientSession() as api:
            route = ScoreRoute.user_scoreboard()
            async with api.get(route) as response:
                return await PageResponse.parse(response, UserScoreResponse)

    @staticmethod
    async def team_scoreboard() -> ApiResponse[PageResponse[TeamScoreResponse]]:
        async with ClientSession() as api:
            route = ScoreRoute.team_scoreboard()
            async with api.get(route) as response:
                return await PageResponse.parse(response, TeamScoreResponse)
