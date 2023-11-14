from django.db import models
from django.urls import reverse

from Frontier.common.models import NormalStringMixin
from django.utils.translation import gettext_lazy as gl


# -------------------------------------------- Abstract Models Section -------------------------------------------------

class AbstractTitanModel(NormalStringMixin, models.Model):
    class Meta:
        abstract = True

    def user_directory_path(instance, filename):
        return "{0}/{1}".format(instance.name, filename)

    name = models.CharField(max_length=255, default='Empty', verbose_name='Имя титана')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    mp_descr = models.TextField(blank=True, verbose_name='Описание на основной странице')
    mp_image = models.ImageField(upload_to=user_directory_path, verbose_name='Фото на основной странице')


class AbstractEquipmentModel(NormalStringMixin, models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255, default='Empty', verbose_name='Название снаряжения')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    descr = models.TextField(blank=False, verbose_name='Описание снаряжения')


class AbstractContentModel(NormalStringMixin, models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255, default='Empty', verbose_name='Имя блока')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    content = models.TextField(verbose_name='Наполнение', null=True)


# ------------------------------------------- Content Models Section ---------------------------------------------------

class ChapterModel(NormalStringMixin, models.Model):
    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    class ChapterType(models.TextChoices):
        TITAN_PAGE = "TP", gl("Главная страница титанов")
        PILOT_PAGE = "PP", gl("Главная страница пилотов")
        UNDEFINED = "UN", gl("Не определено")

    name = models.CharField(max_length=255, default='Empty', verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    upper_text = models.TextField(verbose_name='Вступительный текст')
    lower_text = models.TextField(verbose_name='Концовка главы')
    curr_page = models.CharField(max_length=2, choices=ChapterType.choices, default=ChapterType.UNDEFINED,
                                 verbose_name='Относится к странице:')


class MediaContentBlockModel(AbstractContentModel):
    class Meta:
        verbose_name = 'Основная контентная единица'
        verbose_name_plural = 'Основные контентные единицы'

    def user_directory_path(instance, filename):
        return f"additional/{filename}"

    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True,
                              verbose_name='Ссылка на изображение')
    video_link = models.CharField(max_length=255, blank=True, verbose_name='Ссылка на видео')
    media_descr = models.CharField(max_length=255, verbose_name='Описание фото/видео')
    chapter = models.ForeignKey(to=ChapterModel, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='content', verbose_name='Связанная глава')


# ------------------------------------------- Titan Models Section -----------------------------------------------------

class FirstGenTitanModel(AbstractTitanModel):
    class Meta:
        verbose_name = 'Титан первого поколения'
        verbose_name_plural = 'Титаны первого поколения'


class SecondGenTitanModel(AbstractTitanModel):
    class Meta:
        verbose_name = 'Титан второго поколения'
        verbose_name_plural = 'Титаны второго поколения'

    def get_absolute_url(self):
        return reverse('titan_model', kwargs={'titan_slug': self.slug})

    full_descr = models.TextField(blank=True, verbose_name='Подробное описание')
    video_link = models.CharField(max_length=255, blank=False, verbose_name='Ссылка на видео')
    ancestor_model = models.ForeignKey(to=FirstGenTitanModel, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='children', verbose_name='Модель-предок')


# --------------------------------------- Equipment & Strategy Models Section ------------------------------------------

class TitanWeaponModel(AbstractEquipmentModel):
    class Meta:
        verbose_name = 'Основное снаряжение титанов'
        verbose_name_plural = 'Основное снаряжение титанов'

    class WeaponType(models.TextChoices):
        MAIN_WEAPON = "MW", gl("Основное оружие")
        SUB_WEAPON = "SW", gl("Дополнительное оружие")
        TACTICAL_WEAPON = "TW", gl("Тактическое оружие")
        DEFENCE_WEAPON = "DW", gl("Оборонительное оружие")
        CORE_WEAPON = "CW", gl("Ядро")

    def user_directory_path(instance, filename):
        return "{0}/{1}".format(instance.titan.name, filename)

    weapon_image = models.ImageField(upload_to=user_directory_path, verbose_name='Изображение оружия')
    weapon_type = models.CharField(max_length=2, choices=WeaponType.choices, default=WeaponType.MAIN_WEAPON,
                                   verbose_name='Тип оружия')
    titan = models.ForeignKey(to=SecondGenTitanModel, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='weapon', verbose_name='Титан-владелец')


class TitanKitModel(AbstractEquipmentModel):
    class Meta:
        verbose_name = 'Дополнительный набор титана'
        verbose_name_plural = 'Дополнительные наборы титанов'

    titan = models.ForeignKey(to=SecondGenTitanModel, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='kits', verbose_name='Титан-владелец')


class StrategyBlockModel(AbstractContentModel):
    class Meta:
        verbose_name = 'Блок стратегии'
        verbose_name_plural = 'Блоки стратегии'

    def user_directory_path(instance, filename):
        return "{0}/strategy_pictures/{1}".format(instance.titan.name, filename)

    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True,
                              verbose_name='Ссылка на изображение')
    titan = models.ForeignKey(to=SecondGenTitanModel, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='strategy', verbose_name='Титан-владелец')


#  --------------------------------------------- Only For Monarch ------------------------------------------------------

class MonarchCoreStageModel(NormalStringMixin, models.Model):
    class Meta:
        verbose_name = 'Стадия эволюции Монарха'
        verbose_name_plural = 'Стадии эволюции Монарха'

    stage = models.CharField(max_length=255, default='Empty', verbose_name='Стадия эволюции')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    descr = models.TextField(blank=False, verbose_name='Описание стадии')


class MonarchCoreUpgradeModel(AbstractContentModel):
    class Meta:
        verbose_name = 'Улучшение ядра Монарха'
        verbose_name_plural = 'Улучшения ядра Монарха'

    def user_directory_path(instance, filename):
        return f"Монарх/core_upgrades/{filename}"

    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True,
                              verbose_name='Ссылка на изображение')
    stage = models.ForeignKey(to=MonarchCoreStageModel, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='upgrades', verbose_name='Связанная стадия')
