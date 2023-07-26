from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass
class PageRequest:
    class Direction(Enum):
        ASC = 'ASC'
        DESC = 'DESC'

    page: int = 1
    size: int = 20
    order: str = Direction.ASC.value
    field: str = 'createdAt'
