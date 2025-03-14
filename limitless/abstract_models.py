"""Abstract Django models used in throughout the application."""
from typing import Iterable

from django.db import models


class TimestampModel(models.Model):
    """Provide basic timestamps to models."""

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: str | None = None,
        update_fields: Iterable[str] | None = None,
    ) -> None:
        """Ensure that the `last_modified_at` field is always updated."""
        if update_fields is not None:
            update_fields = list(update_fields)
            if "last_modified_at" not in update_fields:
                update_fields.append("last_modified_at")

        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
