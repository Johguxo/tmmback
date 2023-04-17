# Generated by Django 4.1.7 on 2023-03-16 07:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_specialist'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='signature',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]