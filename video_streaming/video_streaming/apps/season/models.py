from django.db import models

from apps.video.models import Video
from apps.base.models import BaseModel


class Season(BaseModel):
    """Model definition for the serie's season."""

    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name="Video")
    chapters = models.SmallIntegerField(verbose_name="Capitulos", default=8)
    number_season = models.SmallIntegerField(verbose_name="Temporada", default=1)

    class Meta:

        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"

    def __str__(self):
        return f"{self.id} - temporada {self.number_season} - {self.video.name}"

    def to_dict(self):
        return {
            "video": self.video,
            "chapters": self.chapters,
            "number_season": self.number_season,
        }

    @property
    def number_of_seasons(self):
        from django.db.models import Count
        from apps.season.models import Season

        seasons = Season.objects.filter(video=self, state=True).aggregate(
            Count("video")
        )

        return seasons
