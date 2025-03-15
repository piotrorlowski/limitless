from django.db.models import QuerySet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import Profile
from users.serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.none()
    serializer_class = ProfileSerializer

    def get_queryset(self) -> QuerySet[Profile]:
        return Profile.objects.filter(
            user__is_active=True,
            user__is_staff=False,
            user__is_superuser=False,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            profile = serializer.save()
            return Response(
                self.get_serializer(profile).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
