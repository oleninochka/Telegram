from dataclasses import dataclass

from app.api.dto.base import BaseEntity


@dataclass
class TeamResponse(BaseEntity):
    id: str
    name: str
