from django.db.models import QuerySet
from rest_framework.viewsets import ReadOnlyModelViewSet

from users.models import Profile
from users.serializers import ProfileSerializer


class ProfileViewSet(ReadOnlyModelViewSet):
    queryset = Profile.objects.none()
    serializer_class = ProfileSerializer

    def get_queryset(self) -> QuerySet[Profile]:
        return Profile.objects.filter(
            user__is_active=True,
            user__is_staff=False,
            user__is_superuser=False,
        )
