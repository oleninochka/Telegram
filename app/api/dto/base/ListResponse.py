from __future__ import annotations

from dataclasses import dataclass
from typing import List, Type, Dict, TypeVar, Generic

from aiohttp import ClientResponse

from app.api.dto.base import BaseResponse, ApiResponse

T = TypeVar('T', BaseResponse, BaseResponse)


@dataclass
class ListResponse(Generic[T]):
    content: List[T]

    def __init__(self, inner: Type[T], data: Dict[str, List[T]]):
        self.content = [inner.parse(item) for item in data['content']]

    @staticmethod
    async def parse(inner: Type[T], response: ClientResponse) -> ApiResponse[ListResponse[T]]:
        json: Dict = await response.json()
        data = json.get('data', {'content': []})
        return ApiResponse(
            status=response.status,
            message=json.get('message', None),
            data=ListResponse(inner, data),
        )
