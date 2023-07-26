from dataclasses import dataclass

from app.api.dto.base import BaseResponse


@dataclass
class TeamResponse(BaseResponse):
    id: str
    name: str
