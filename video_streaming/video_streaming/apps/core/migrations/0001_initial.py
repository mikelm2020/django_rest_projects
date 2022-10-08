# Generated by Django 4.1.2 on 2022-10-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Classification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "age_rating",
                    models.CharField(max_length=5, verbose_name="Clasificación"),
                ),
            ],
            options={
                "verbose_name": "Clasificación",
                "verbose_name_plural": "Clasificaciones",
            },
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", models.CharField(max_length=50, verbose_name="País")),
                ("iso_code", models.CharField(max_length=3, verbose_name="Codigo ISO")),
            ],
            options={
                "verbose_name": "País",
                "verbose_name_plural": "Paises",
            },
        ),
        migrations.CreateModel(
            name="FilmGenre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "film_genre",
                    models.CharField(
                        max_length=50, verbose_name="Genero cinematográfico"
                    ),
                ),
            ],
            options={
                "verbose_name": "Genero",
                "verbose_name_plural": "Generos",
            },
        ),
        migrations.CreateModel(
            name="Provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("provider", models.CharField(max_length=15, verbose_name="Proveedor")),
            ],
            options={
                "verbose_name": "Proveedor",
                "verbose_name_plural": "Proveedores",
            },
        ),
    ]
