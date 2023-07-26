from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Type, Dict, TypeVar, Optional

from aiohttp import ClientResponse

from app.backend.dto.base import BaseDto
from app.backend.dto.container import ListResponse
from app.backend.dto.container import PageResponse

T = TypeVar('T', BaseDto, BaseDto)


@dataclass
class ApiResponse(Generic[T]):
    status: int
    data: Optional[T] | ListResponse[T] | PageResponse[T]
    message: Optional[str] = None

    @staticmethod
    async def parse(inner: Type[T], response: ClientResponse) -> ApiResponse[T]:
        json: Dict = await response.json()
        data = inner.parse(json['data']) if 'data' in json else None
        return ApiResponse(
            status=response.status,
            data=data,
            message=json.get('message', None),
        )

    @staticmethod
    async def parse_message(response: ClientResponse) -> ApiResponse[T]:
        json: Dict = await response.json()
        return ApiResponse(
            status=response.status,
            data=None,
            message=json.get('message', None),
        )

    @staticmethod
    async def parse_page(inner: Type[T], response: ClientResponse) -> ApiResponse[PageResponse[T]]:
        json: Dict = await response.json()
        return ApiResponse(
            status=response.status,
            data=PageResponse.parse(inner, json['data']),
        )
