from dataclasses import dataclass
from typing import Dict

from app.api.dto.base import BaseResponse
from app.api.dto.team import TeamResponse


@dataclass
class TeamScoreResponse(BaseResponse):
    score: float
    team: TeamResponse

    @classmethod
    def parse(cls, data: Dict):
        if data is None:
            return None
        return TeamScoreResponse(score=data["score"], team=TeamResponse.parse(data["team"]))
