# Generated by Django 4.2.5 on 2023-09-27 22:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cultures_app', '0004_rename_description_clan_exceptional_male_names_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clan',
            name='exceptional_female_names',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]