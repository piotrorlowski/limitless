import logging
from typing import ClassVar

from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import AbstractUser
from django.db import models

from limitless.abstract_models import TimestampModel
from users.managers import UserManager

logger = logging.getLogger(__name__)


class User(TimestampModel, AbstractUser):
    username = None  # type: ignore
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    objects: ClassVar[UserManager] = UserManager()  # type: ignore

    def __str__(self) -> str:
        if self.first_name:
            return f"{self.first_name} {self.last_name} <{self.email}>"
        return self.email


class Profile(TimestampModel):
    user = AutoOneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )

    bio = models.TextField("bio", blank=True)
    avatar = models.ImageField(
        "avatar", upload_to="avatars/", blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.user.email} profile"
