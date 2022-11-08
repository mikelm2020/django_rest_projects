from rest_framework import serializers
from apps.season.models import Season


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        exclude = (
            "state",
            "created_date",
            "modified_date",
            "deleted_date",
        )


class VideoOnSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ("video",)
