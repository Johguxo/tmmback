# Generated by Django 4.1.7 on 2023-04-17 06:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_alter_label_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
