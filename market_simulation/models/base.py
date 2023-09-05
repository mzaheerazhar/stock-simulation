import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
        ordering = ["-created_at"]
