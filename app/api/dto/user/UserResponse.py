from dataclasses import dataclass
from typing import Optional

from app.api.dto.base import BaseResponse
from app.api.dto.team import TeamResponse


@dataclass
class UserResponse(BaseResponse):
    id: str
    name: str
    team: Optional[TeamResponse] = None
    admin: bool = False
