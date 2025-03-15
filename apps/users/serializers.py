from typing import Any

from rest_framework import serializers, validators

from users.constants import INVALID_IMAGE_FORMAT, REQUIRED_FIELD_ERRORS
from users.models import Profile, User


class UserField(serializers.RelatedField):
    def to_representation(self, instance: User) -> dict[str, str]:
        return {
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
        }


class UserFieldReadMixin(serializers.Serializer):
    user = UserField(read_only=True)


class ProfileFieldsCreateMixin(serializers.Serializer):
    first_name = serializers.CharField(
        write_only=True,
        error_messages=dict(REQUIRED_FIELD_ERRORS),
    )
    last_name = serializers.CharField(
        write_only=True,
        error_messages=dict(REQUIRED_FIELD_ERRORS),
    )
    email = serializers.EmailField(
        write_only=True,
        validators=[
            validators.UniqueValidator(
                queryset=User.objects.all(),  # type: ignore
                message="Email already registered.",
            )
        ],
        error_messages=dict(REQUIRED_FIELD_ERRORS),
    )


class ProfileSerializer(
    serializers.ModelSerializer, UserFieldReadMixin, ProfileFieldsCreateMixin
):
    bio = serializers.CharField(required=False)
    avatar = serializers.ImageField(
        required=False,
        error_messages=dict(INVALID_IMAGE_FORMAT),
    )

    class Meta:
        model = Profile
        exclude: list[str] = []

    def create(self, validated_data: dict[str, Any]) -> Profile:
        user = User.objects.create(
            first_name=validated_data.pop("first_name"),
            last_name=validated_data.pop("last_name"),
            email=validated_data.pop("email"),
        )
        profile = Profile.objects.create(user=user, **validated_data)
        return profile
