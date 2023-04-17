# Generated by Django 4.1.7 on 2023-03-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0007_machine_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidentsmachine',
            name='machine',
        ),
        migrations.AddField(
            model_name='incidentsmachine',
            name='subtitle',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='incidentsmachine',
            name='title',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]