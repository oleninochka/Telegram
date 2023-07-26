from dataclasses import dataclass

from app.backend.dto.base import BaseEntity


@dataclass
class ChallengeResponse(BaseEntity):
    id: str
    name: str
    description: str
    weight: float
    team: bool
    visible: bool
