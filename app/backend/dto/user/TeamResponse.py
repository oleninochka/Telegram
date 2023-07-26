from dataclasses import dataclass

from app.backend.dto.base import BaseEntity


@dataclass
class TeamResponse(BaseEntity):
    id: str
    name: str
