from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from apps.season.api.season_serializers import SeasonSerializer, VideoOnSeasonSerializer
from apps.season.models import Season


class SeasonViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return Season.objects.filter(state=True)
        else:
            return Season.objects.filter(id=pk, state=True).first()

    def get_object(self, pk):
        return get_object_or_404(Season, pk=pk)

    def list(self, request):
        season_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(season_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Temporada registrada correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Hay errores en el registro", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def retrieve(self, request, pk=None):
        video = self.get_object(pk)
        video_serializer = self.serializer_class(video)
        return Response(video_serializer.data)

    def update(self, request, pk=None):
        video = self.get_object(pk)
        video_serializer = self.serializer_class(video, data=request.data)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(
                {"message": "Video actualizado correctamente"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Hay errores en la actualización",
                "error": video_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, pk=None):
        video_destroy = self.serializer_class.Meta.model.objects.filter(id=pk).update(
            state=False
        )
        if video_destroy == 1:
            return Response(
                {"message": "Video eliminado correctamente!"}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "No existe el video que desea eliminar"},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(methods=["get"], detail=False)
    def search_video(self, request):
        """
        Search the serie with at least one season
        """
        video_searched = request.query_params.get("video_searched", "")
        video = Season.objects.filter(video=video_searched).first()
        if video:
            video_serializer = VideoOnSeasonSerializer(video)
            return Response(video_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"message": "El video no es una serie"}, status=status.HTTP_404_NOT_FOUND
        )
