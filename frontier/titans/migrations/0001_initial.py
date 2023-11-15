# Generated by Django 4.2.7 on 2023-11-14 09:49

import Frontier.common.models
from django.db import migrations, models
import django.db.models.deletion
import titans.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Empty', max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('upper_text', models.TextField(verbose_name='Вступительный текст')),
                ('lower_text', models.TextField(verbose_name='Концовка главы')),
                ('curr_page', models.CharField(choices=[('TP', 'Главная страница титанов'), ('PP', 'Главная страница пилотов'), ('UN', 'Не определено')], default='UN', max_length=2, verbose_name='Относится к странице:')),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Главы',
            },
            bases=(Frontier.common.models.NormalStringMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FirstGenTitanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Empty', max_length=255, verbose_name='Имя титана')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('mp_descr', models.TextField(blank=True, verbose_name='Описание на основной странице')),
                ('mp_image', models.ImageField(upload_to=titans.models.AbstractTitanModel.user_directory_path, verbose_name='Фото на основной странице')),
            ],
            options={
                'verbose_name': 'Титан первого поколения',
                'verbose_name_plural': 'Титаны первого поколения',
            },
            bases=(Frontier.common.models.NormalStringMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MonarchCoreStageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(default='Empty', max_length=255, verbose_name='Стадия эволюции')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('descr', models.TextField(verbose_name='Описание стадии')),
            ],
            options={
                'verbose_name': 'Стадия эволюции Монарха',
                'verbose_name_plural': 'Стадии эволюции Монарха',
            },
            bases=(Frontier.common.models.NormalStringMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SecondGenTitanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Empty', max_length=255, verbose_name='Имя титана')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('mp_descr', models.TextField(blank=True, verbose_name='Описание на основной странице')),
                ('mp_image', models.ImageField(upload_to=titans.models.AbstractTitanModel.user_directory_path, verbose_name='Фото на основной странице')),
                ('full_descr', models.TextField(blank=True, verbose_name='Подробное описание')),
                ('video_link', models.CharField(max_length=255, verbose_name='Ссылка на видео')),
                ('ancestor_model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='titans.firstgentitanmodel', verbose_name='Модель-предок')),
            ],
            options={
                'verbose_name': 'Титан второго поколения',
                'verbose_name_plural': 'Титаны второго поколения',
            },
            bases=(Frontier.common.models.NormalStringMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TitanWeaponModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Empty', max_length=255, verbose_name='Название снаряжения')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('descr', models.TextField(verbose_name='Описание снаряжения')),
                ('weapon_image', models.ImageField(upload_to=titans.models.TitanWeaponModel.user_directory_path, verbose_name='Изображение оружия')),
                ('weapon_type', models.CharField(choices=[('MW', 'Основное оружие'), ('SW', 'Дополнительное оружие'), ('TW', 'Тактическое оружие'), ('DW', 'Оборонительное оружие'), ('CW', 'Ядро')], default='MW', max_length=2, verbose_name='Тип оружия')),
                ('titan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='weapon', to='titans.secondgentitanmodel', verbose_name='Титан-владелец')),
            ],
            options={
                'verbose_name': 'Основное снаряжение титанов',
                'verbose_name_plural': 'Основное снаряжение титанов',
            },
            bases=(Frontier.common.models.NormalStringMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TitanKitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Empty', max_length=255, verbose_name='Название снаряжения')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('descr', models.TextField(verbose_name='Описание снаряжения')),
                ('titan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kits', to='titans.secondgentitanmodel', verbose_name='Титан-владелец')),
            ],
            options={
                'verbose_name': 'Дополнительный набор титана',
                'verbose_name_plural': 'Дополнительные наборы титанов',
            },
            bases=(Frontier.common.models.NormalStringMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StrategyBlockModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Empty', max_length=255, verbose_name='Имя блока')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('content', models.TextField(null=True, verbose_name='Наполнение')),
                ('image', models.ImageField(blank=True, null=True, upload_to=titans.models.StrategyBlockModel.user_directory_path, verbose_name='Ссылка на изображение')),
                ('titan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='strategy', to='titans.secondgentitanmodel', verbose_name='Титан-владелец')),
            ],
            options={
                'verbose_name': 'Блок стратегии',
                'verbose_name_plural': 'Блоки стратегии',
            },
        ),
        migrations.CreateModel(
            name='MonarchCoreUpgradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Empty', max_length=255, verbose_name='Имя блока')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('content', models.TextField(null=True, verbose_name='Наполнение')),
                ('image', models.ImageField(blank=True, null=True, upload_to=titans.models.MonarchCoreUpgradeModel.user_directory_path, verbose_name='Ссылка на изображение')),
                ('stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='upgrades', to='titans.monarchcorestagemodel', verbose_name='Связанная стадия')),
            ],
            options={
                'verbose_name': 'Улучшение ядра Монарха',
                'verbose_name_plural': 'Улучшения ядра Монарха',
            },
        ),
        migrations.CreateModel(
            name='MediaContentBlockModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Empty', max_length=255, verbose_name='Имя блока')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('content', models.TextField(null=True, verbose_name='Наполнение')),
                ('image', models.ImageField(blank=True, null=True, upload_to=titans.models.MediaContentBlockModel.user_directory_path, verbose_name='Ссылка на изображение')),
                ('video_link', models.CharField(blank=True, max_length=255, verbose_name='Ссылка на видео')),
                ('media_descr', models.CharField(max_length=255, verbose_name='Описание фото/видео')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content', to='titans.chaptermodel', verbose_name='Связанная глава')),
            ],
            options={
                'verbose_name': 'Основная контентная единица',
                'verbose_name_plural': 'Основные контентные единицы',
            },
        ),
    ]
