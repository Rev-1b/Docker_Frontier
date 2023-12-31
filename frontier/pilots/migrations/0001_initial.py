# Generated by Django 5.0 on 2023-12-20 12:28

import Frontier.common.models
import django.db.models.deletion
import pilots.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PilotModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Слаг')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('mp_descr', models.TextField(blank=True)),
                ('mp_logo', models.ImageField(upload_to=pilots.models.PilotModel.user_directory_path, verbose_name='Логотип')),
                ('short_descr', models.TextField(blank=True)),
                ('features', models.TextField(blank=True, verbose_name='Особенности')),
            ],
            options={
                'verbose_name': 'Пилот',
                'verbose_name_plural': 'Пилоты',
            },
            bases=(Frontier.common.models.NormalStringMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CarouselImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Слаг')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(blank=True, db_index=True, null=True, upload_to=pilots.models.CarouselImagesModel.user_directory_path, verbose_name='Ссылка на изображение')),
                ('pilot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carousel', to='pilots.pilotmodel', verbose_name='Пилот-владелец')),
            ],
        ),
        migrations.CreateModel(
            name='PilotStrategyBlockModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Empty', max_length=255, verbose_name='Имя блока')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('content', models.TextField(null=True, verbose_name='Наполнение')),
                ('image', models.ImageField(blank=True, db_index=True, null=True, upload_to=pilots.models.PilotStrategyBlockModel.user_directory_path, verbose_name='Ссылка на изображение')),
                ('pilot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='strategy', to='pilots.pilotmodel', verbose_name='Пилот-владелец')),
            ],
            options={
                'verbose_name': 'Блок стратегии',
                'verbose_name_plural': 'Блоки стратегии',
            },
            bases=(Frontier.common.models.NormalStringMixin, models.Model),
        ),
    ]
