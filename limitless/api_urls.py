from rest_framework.routers import SimpleRouter

from apps.users import api as users_api

router = SimpleRouter()
router.register("profile", users_api.ProfileViewSet)
