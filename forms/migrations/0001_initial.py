# Generated by Django 4.1.7 on 2023-02-22 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.form')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SectionForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default='', max_length=200)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.form')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'TEXT'), (1, 'CHECKBOX'), (3, 'MULTISELECT'), (4, 'RADIO')], default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.question')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerUserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.userform')),
            ],
        ),
    ]
