from rest_framework.routers import DefaultRouter

from apps.season.api.season_viewsets import SeasonViewSet

router = DefaultRouter()
router.register(r"", SeasonViewSet, basename="seasons")
urlpatterns = router.urls
