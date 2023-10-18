from rest_framework import routers

from users.views import UserViewSet

from users.apps import UsersConfig

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='users')