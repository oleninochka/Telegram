from dataclasses import dataclass
from typing import Optional

from app.api.dto.base import BaseResponse


@dataclass
class EventResponse(BaseResponse):
    id: str
    title: str
    speaker: str
    affiliate: Optional[str]
    start: str
    end: str
