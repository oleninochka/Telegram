from __future__ import annotations

from dataclasses import dataclass
from typing import List, Type, Dict, TypeVar, Generic

from aiohttp import ClientResponse

from app.api.dto.base import ApiResponse, BaseResponse
from app.api.dto.base.Serializable import Serializable

T = TypeVar("T", BaseResponse, BaseResponse)


@dataclass
class PageResponse(Generic[T], Serializable):
    content: List[T]
    totalPages: int
    page: int
    size: int

    def __init__(self, inner: Type[T], data: Dict[str, List[T] | int]):
        self.content = [inner.parse(item) for item in data["content"]]
        self.page = data["page"]
        self.size = data["size"]
        self.totalPages = data["totalPages"]

    @staticmethod
    async def parse(response: ClientResponse, inner: Type[T]) -> ApiResponse[PageResponse[T]]:
        json: Dict = await response.json()
        data = json.get("data", {"content": []})
        return ApiResponse(
            status=response.status,
            message=json.get("message", None),
            data=PageResponse(inner, data),
        )
