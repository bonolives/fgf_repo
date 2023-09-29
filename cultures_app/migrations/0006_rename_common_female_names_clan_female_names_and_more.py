# Generated by Django 4.2.5 on 2023-09-28 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cultures_app', '0005_clan_exceptional_female_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clan',
            old_name='common_female_names',
            new_name='female_names',
        ),
        migrations.RenameField(
            model_name='clan',
            old_name='common_male_names',
            new_name='lead_god',
        ),
        migrations.RenameField(
            model_name='clan',
            old_name='exceptional_female_names',
            new_name='male_names',
        ),
        migrations.RenameField(
            model_name='clan',
            old_name='exceptional_male_names',
            new_name='other_deities',
        ),
        migrations.RenameField(
            model_name='clan',
            old_name='known_deities',
            new_name='reserved_female_names',
        ),
        migrations.RenameField(
            model_name='clan',
            old_name='known_headgod',
            new_name='reserved_male_names',
        ),
    ]