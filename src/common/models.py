from django.db import models
from django.db.models import Manager


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="등록일"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    objects = Manager()

    _TO_DICT_FILED_LIST = ["id"]

    class Meta:
        abstract = True
