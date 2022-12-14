from rest_framework import serializers
from apps.core.models import *


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
