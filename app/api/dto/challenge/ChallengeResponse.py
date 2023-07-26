from dataclasses import dataclass
from typing import Optional

from app.api.dto.base import BaseEntity


@dataclass
class ChallengeResponse(BaseEntity):
    id: str
    name: str
    description: str
    weight: float
    team: bool
    visible: bool
    start: Optional[str]
    end: Optional[str]
