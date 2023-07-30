from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from app.api.dto.base import BaseResponse


@dataclass
class ChallengeResponse(BaseResponse):
    id: str
    name: str
    description: Optional[str]
    weight: float
    team: bool
    visible: bool
    start: Optional[datetime]
    end: Optional[datetime]
    solved: bool
