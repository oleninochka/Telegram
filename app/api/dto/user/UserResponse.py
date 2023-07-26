from dataclasses import dataclass
from typing import Optional

from app.api.dto.base import BaseEntity
from app.api.dto.user import TeamResponse


@dataclass
class UserResponse(BaseEntity):
    id: str
    name: str
    team: Optional[TeamResponse] = None
