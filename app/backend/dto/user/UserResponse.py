from dataclasses import dataclass
from typing import Optional

from app.backend.dto.base import BaseEntity
from app.backend.dto.user import TeamResponse


@dataclass
class UserResponse(BaseEntity):
    id: str
    name: str
    team: Optional[TeamResponse] = None
