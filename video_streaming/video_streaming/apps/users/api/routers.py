from nturl2path import url2pathname
from rest_framework.routers import DefaultRouter

from apps.users.api.api import UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet, basename="users")
urlpatterns = router.urls
