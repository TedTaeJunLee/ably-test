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

    @classmethod
    def get_by_id(cls, model_id: int) -> Any:
        return cls.get_queryset().get(id=model_id)

    @classmethod
    def save(cls, entities: List, update_fields: List) -> List:
        for entity in entities:
            entity.save(update_fields=update_fields)

        return entities
