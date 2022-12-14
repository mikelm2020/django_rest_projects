# Generated by Django 4.1.1 on 2022-10-05 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalproduct",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Producto",
                "verbose_name_plural": "historical Productos",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Producto", "verbose_name_plural": "Productos"},
        ),
        migrations.RenameField(
            model_name="categoryproduct",
            old_name="delete_date",
            new_name="deleted_date",
        ),
        migrations.RenameField(
            model_name="historicalcategoryproduct",
            old_name="delete_date",
            new_name="deleted_date",
        ),
        migrations.RenameField(
            model_name="historicalindicator",
            old_name="delete_date",
            new_name="deleted_date",
        ),
        migrations.RenameField(
            model_name="historicalmeasureunit",
            old_name="delete_date",
            new_name="deleted_date",
        ),
        migrations.RenameField(
            model_name="historicalproduct",
            old_name="delete_date",
            new_name="deleted_date",
        ),
        migrations.RenameField(
            model_name="indicator",
            old_name="delete_date",
            new_name="deleted_date",
        ),
        migrations.RenameField(
            model_name="measureunit",
            old_name="delete_date",
            new_name="deleted_date",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="delete_date",
            new_name="deleted_date",
        ),
    ]
