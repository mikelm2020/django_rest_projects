from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import (
    MeasureUnitSerializer,
    IndicatorSerializer,
    CategoryProductSerializer,
)


class MeasureUnitListAPIVew(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIVew(GeneralListAPIView):
    serializer_class = IndicatorSerializer


class CategoryProductListAPIVew(GeneralListAPIView):
    serializer_class = CategoryProductSerializer
