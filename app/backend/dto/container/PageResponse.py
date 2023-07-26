from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, List, Type, Dict, TypeVar

from app.backend.dto.base import BaseDto

T = TypeVar('T', BaseDto, BaseDto)


@dataclass
class PageResponse(Generic[T]):
    content: List[T]
    totalPages: int
    page: int
    size: int

    @staticmethod
    def parse(inner: Type[T], data: Dict) -> PageResponse[T]:
        return PageResponse(
            content=[inner.parse(item) for item in data['content']],
            totalPages=data['totalPages'],
            page=data['page'],
            size=data['size'],
        )
