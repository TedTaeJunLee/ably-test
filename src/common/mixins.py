from django.db import models
from django.utils import timezone


class SoftDeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False, verbose_name="삭제 여부")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="삭제일")

    def delete(self, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()

    class Meta:
        abstract = True
