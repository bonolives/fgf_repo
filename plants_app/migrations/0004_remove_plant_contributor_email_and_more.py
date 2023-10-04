# Generated by Django 4.2.3 on 2023-10-01 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_app', '0003_medicinalplant_medicinal_values_entered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='contributor_email',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='contributor_is_source',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='contributor_phone',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='source_email',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='source_name',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='source_phone',
        ),
        migrations.AlterField(
            model_name='plant',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media_files'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='life_form',
            field=models.CharField(choices=[('shrub', 'Shrub'), ('tree', 'Tree'), ('herb', 'Herb'), ('grass', 'Grass'), ('climber', 'Climber'), ('other', 'Other')], max_length=250),
        ),
        migrations.AlterField(
            model_name='plant',
            name='publish_preference',
            field=models.CharField(blank=True, choices=[('name_and_email', 'Name and Email'), ('name_only', 'Name Only'), ('none', 'Do Not Publish')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='region',
            field=models.CharField(choices=[('Northern Uganda', 'Northern Uganda'), ('West Nile', 'West Nile'), ('Central Uganda', 'Central Uganda'), ('Eastern Uganda', 'Eastern Uganda'), ('Western Uganda', 'Western Uganda'), ('All Regions', 'All Regions')], max_length=50),
        ),
        migrations.AlterField(
            model_name='plant',
            name='value',
            field=models.CharField(choices=[('ecological', 'Ecological'), ('social', 'Social'), ('economic', 'Economic'), ('nutritional', 'Nutritional'), ('other', 'Other')], max_length=250),
        ),
    ]