from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from app.api.dto.base import BaseResponse


@dataclass
class EventResponse(BaseResponse):
    id: str
    title: str
    description: Optional[str]
    speaker: Optional[str]
    affiliate: Optional[str]
    start: datetime
    end: datetime
