# Generated by Django 4.1.2 on 2022-11-11 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("playlist", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="historicalplaylist",
            old_name="usuario",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="playlist",
            old_name="usuario",
            new_name="user",
        ),
    ]
