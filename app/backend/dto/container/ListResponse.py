from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, List, Type, Dict, TypeVar

from app.backend.dto.base import BaseDto

T = TypeVar('T', BaseDto, BaseDto)


@dataclass
class ListResponse(Generic[T]):
    content: List[T]

    @staticmethod
    def parse(inner: Type[T], data: Dict) -> ListResponse[T]:
        return ListResponse(content=[inner.parse(item) for item in data['content']])
