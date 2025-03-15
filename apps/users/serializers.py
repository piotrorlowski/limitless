from rest_framework import serializers

from users.models import Profile, User


class UserField(serializers.RelatedField):
    def to_representation(self, instance):
        return {
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
        }


class ProfileSerializer(serializers.ModelSerializer):
    user = UserField(read_only=True)
    bio = serializers.CharField(required=False)
    avatar = serializers.ImageField(required=False)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    def to_internal_value(self, data):
        return super().to_internal_value(data)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "bio",
            "avatar",
            "first_name",
            "last_name",
            "email",
        )

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data.pop("first_name"),
            last_name=validated_data.pop("last_name"),
            email=validated_data.pop("email"),
        )
        profile = Profile.objects.create(user=user, **validated_data)
        return profile
