from __future__ import annotations

from dataclasses import dataclass
from types import NoneType
from typing import Generic, Type, Dict, TypeVar, Optional

from aiohttp import ClientResponse

from app.api.dto.base import BaseResponse
from app.api.dto.base.Serializable import Serializable

T = TypeVar("T", Serializable, BaseResponse)


@dataclass
class ApiResponse(Generic[T], Serializable):
    status: int
    message: Optional[str]
    data: Optional[T]

    @staticmethod
    async def parse(response: ClientResponse, inner: Type[T] = NoneType) -> ApiResponse[T]:
        json: Dict = await response.json()
        data = inner.parse(json["data"]) if "data" in json else None
        return ApiResponse(
            status=response.status,
            message=json.get("message", None),
            data=data,
        )
