# Generated by Django 4.1.7 on 2023-02-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidentsmachine',
            name='video',
        ),
        migrations.RemoveField(
            model_name='info',
            name='video',
        ),
        migrations.AddField(
            model_name='incidentsmachine',
            name='video_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='info',
            name='video_link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
