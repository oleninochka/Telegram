from dataclasses import dataclass

from app.api.dto.base import Serializable


@dataclass
class ParticipateRequest(Serializable):
    userId: str
    invite: str
