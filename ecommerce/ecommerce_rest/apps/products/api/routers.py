from rest_framework.routers import DefaultRouter

from apps.products.api.viewsets.product_viewsets import ProductViewSet
from apps.products.api.viewsets.general_views import *


router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"measure-units", MeasureUnitViewSet, basename="measure_units")
router.register(r"indicators", IndicatorViewSet, basename="indicators")
router.register(
    r"category-products", CategoryProductViewSet, basename="category_products"
)

urlpatterns = router.urls
