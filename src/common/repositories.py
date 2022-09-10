from abc import ABC
from typing import Any, List, Type

from django.db.models import Manager
from src.common.models import BaseModel


class BaseRepository(ABC):
    model_class: Type[BaseModel]

    @classmethod
    def get_queryset(cls) -> Manager[Any]:
        return cls.model_class.objects

    @classmethod
    def create(cls, entities: List) -> List:
        for entity in entities:
            entity.save(force_insert=True)

        return entities
