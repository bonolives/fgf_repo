# Generated by Django 4.2.6 on 2023-11-05 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0003_alter_animal_citation_alter_animallocalname_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='animal_audios'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='animal_images'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='animal_videos'),
        ),
    ]
