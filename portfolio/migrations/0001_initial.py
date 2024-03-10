# Generated by Django 5.0.3 on 2024-03-10 17:37

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('date_started', models.DateField(default=datetime.date.today)),
                ('date_released', models.DateField(default=datetime.date.today)),
                ('repo_link', models.URLField(max_length=300)),
                ('slug', models.SlugField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(3, message='Минимум 5 символов'), django.core.validators.MaxLengthValidator(200, message='Максимум 200 символов')])),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/', verbose_name='фото')),
                ('is_released', models.BooleanField(default=False)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='portfolio.role')),
                ('tags', models.ManyToManyField(blank=True, related_name='projects', to='portfolio.tag')),
            ],
        ),
    ]