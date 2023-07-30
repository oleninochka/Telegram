from dataclasses import dataclass
from typing import Dict

from app.api.dto.base import BaseResponse
from app.api.dto.score.TeamScoreResponse import TeamScoreResponse
from app.api.dto.score.UserScoreResponse import UserScoreResponse


@dataclass
class ProfileScoreResponse(BaseResponse):
    user: UserScoreResponse
    team: TeamScoreResponse

    @classmethod
    def parse(cls, data: Dict):
        return ProfileScoreResponse(
            user=UserScoreResponse.parse(data["user"]),
            team=TeamScoreResponse.parse(data["team"]),
        )
