from __future__ import annotations

from dataclasses import dataclass
from types import NoneType
from typing import Generic, Type, Dict, TypeVar, Optional, Any

from aiohttp import ClientResponse

from app.api.dto.base import BaseResponse

T = TypeVar('T', BaseResponse, BaseResponse)


@dataclass
class ApiResponse(Generic[T]):
    status: int
    message: Optional[str]
    data: Optional[T] | Optional[Any]

    @staticmethod
    async def parse(response: ClientResponse, inner: Type[T] = NoneType) -> ApiResponse[T]:
        json: Dict = await response.json()
        data = inner.parse(json['data']) if 'data' in json else None
        return ApiResponse(
            status=response.status,
            message=json.get('message', None),
            data=data,
        )
