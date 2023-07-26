from dataclasses import asdict

from aiohttp import ClientSession

from app.api.dto.challenge import ChallengeResponse, SubmitRequest
from app.api.dto.container import ApiResponse, PageResponse
from app.api.route import ChallengeRoute


class ChallengeService:
    @staticmethod
    async def list_challenges() -> ApiResponse[PageResponse[ChallengeResponse]]:
        async with ClientSession() as api:
            route = ChallengeRoute.list_challenges()
            async with api.get(route) as response:
                return await ApiResponse.parse_page(ChallengeResponse, response)

    @staticmethod
    async def find_by_id(challenge_id: str) -> ApiResponse[ChallengeResponse]:
        async with ClientSession() as api:
            route = ChallengeRoute.find_by_id(challenge_id)
            async with api.get(route) as response:
                return await ApiResponse.parse(ChallengeResponse, response)

    @staticmethod
    async def submit(challenge_id: str, request: SubmitRequest) -> ApiResponse:
        async with ClientSession() as api:
            route = ChallengeRoute.submit(challenge_id)
            async with api.post(route, json=asdict(request)) as response:
                return await ApiResponse.parse_message(response)
