from rest_framework import serializers
from apps.video.models import Video
from apps.season.models import Season
from apps.core.models import *
from apps.core.api.core_serializers import *


class VideoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Video

        exclude = (
            "state",
            "created_date",
            "modified_date",
            "deleted_date",
        )

        def validate_duration(self, value):
            if value == 0:
                raise serializers.ValidationError(
                    "La duración de una pélicula no puede ser 0"
                )
            return value


class SeasonRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ("video", "chapters", "number_season")

    def save(self):

        new_season = Season.objects.create(**self.validated_data)
        return new_season


class FilmGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmGenre
        fields = ("id", "film_genre")


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ("id", "age_rating")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "country")


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("id", "provider")
