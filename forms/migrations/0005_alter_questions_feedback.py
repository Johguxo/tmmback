# Generated by Django 4.1.7 on 2023-03-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_alter_questions_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='feedback',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
