from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, TypeVar, Type, Generic, Optional

import dacite
from aiohttp import ClientResponse


class BaseDto(ABC):
    @classmethod
    @abstractmethod
    def parse(cls, data: Dict):
        pass


class BaseEntity(BaseDto):
    @classmethod
    def parse(cls, data: Dict):
        return dacite.from_dict(cls, data)


T = TypeVar('T', BaseDto, BaseDto)


@dataclass
class ListResponse(Generic[T]):
    content: List[T]

    @staticmethod
    def parse(inner: Type[T], data: Dict) -> ListResponse[T]:
        return ListResponse(content=[inner.parse(item) for item in data['content']])


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
