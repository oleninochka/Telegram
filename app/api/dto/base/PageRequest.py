from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from app.api.dto.base.Serializable import Serializable


@dataclass
class PageRequest(Serializable):
    class Direction(Enum):
        ASC = "ASC"
        DESC = "DESC"

    page: int = 1
    size: int = 20
    order: str = Direction.ASC.value
    field: str = "createdAt"
