from django.db import models

from apps.video.models import Video
from apps.base.models import BaseModel


class Season(BaseModel):
    """Model definition for the serie's season."""

    video = models.OneToOneField(Video, on_delete=models.CASCADE, primary_key=True)
    chapters = models.SmallIntegerField(verbose_name="Capitulos", default=8)
    number_season = models.SmallIntegerField(verbose_name="Temporada", default=1)

    class Meta:

        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"

    def __str__(self):
        return f"temporada {self.number_season} - {self.video.name}"
