from rest_framework import viewsets
from rest_framework.response import Response

from apps.products.api.serializers.general_serializers import (
    MeasureUnitSerializer,
    IndicatorSerializer,
    CategoryProductSerializer,
)


class MeasureUnitViewSet(viewsets.GenericViewSet):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)


class IndicatorViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)


class CategoryProductViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)
