from typing import TYPE_CHECKING, Any, cast

from django.contrib.auth.base_user import BaseUserManager

if TYPE_CHECKING:
    from users.models import User


class UserManager(BaseUserManager["User"]):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(
        self, email: str, password: str | None, **extra_fields: Any
    ) -> "User":
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = cast("User", self.model(email=email, **extra_fields))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email: str, password: str | None = None, **extra_fields: Any
    ) -> "User":
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            email=email, password=password, **extra_fields
        )

    def create_superuser(
        self, email: str, password: str, **extra_fields: Any
    ) -> "User":
        """Create and save a SuperUser with the given email and password."""
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        return self._create_user(
            email=email, password=password, **extra_fields
        )

    def get_by_natural_key(self, username: str | None) -> "User":
        """Return User instance based on the User email.

        Overridden to make the login email case-insensitive.
        """
        return cast("User", self.get(email__iexact=username))
