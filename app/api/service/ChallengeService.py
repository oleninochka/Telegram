from aiohttp import ClientSession

from app.api.dto.base import ApiResponse, PageResponse, PageRequest
from app.api.dto.challenge import ChallengeResponse, SubmitRequest
from app.api.route import ChallengeRoute


class ChallengeService:
    @staticmethod
    async def list_challenges(user_id: str) -> ApiResponse[PageResponse[ChallengeResponse]]:
        async with ClientSession() as api:
            route = ChallengeRoute.list_challenges()
            params = PageRequest(size=1_000_000).as_json()
            params.update({"userId": user_id})
            async with api.get(route, params=params) as response:
                return await PageResponse.parse(response, ChallengeResponse)

    @staticmethod
    async def find_by_id(challenge_id: str, user_id: str) -> ApiResponse[ChallengeResponse]:
        async with ClientSession() as api:
            route = ChallengeRoute.find_by_id(challenge_id)
            params = {"userId": user_id}
            async with api.get(route, params=params) as response:
                return await ApiResponse.parse(response, ChallengeResponse)

    @staticmethod
    async def submit(challenge_id: str, request: SubmitRequest) -> ApiResponse:
        async with ClientSession() as api:
            route = ChallengeRoute.submit(challenge_id)
            async with api.post(route, json=request.as_json()) as response:
                return await ApiResponse.parse(response)
