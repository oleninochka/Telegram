from dataclasses import dataclass
from typing import Dict

from app.api.dto.base import BaseResponse
from app.api.dto.user import UserResponse


@dataclass
class UserScoreResponse(BaseResponse):
    score: float
    user: UserResponse

    @classmethod
    def parse(cls, data: Dict):
        return UserScoreResponse(score=data["score"], user=UserResponse.parse(data["user"]))
