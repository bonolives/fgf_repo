# Generated by Django 4.2.5 on 2023-09-22 14:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("plants_app", "0002_rename_areas_in_uganda_plant_regions_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Medicinal_Plant",
            new_name="MedicinalPlant",
        ),
        migrations.RenameModel(
            old_name="Medicinal_Use",
            new_name="MedicinalUse",
        ),
    ]