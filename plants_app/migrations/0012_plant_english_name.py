# Generated by Django 4.2.6 on 2023-11-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_app', '0011_alter_plant_region_in_uganda'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='english_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
