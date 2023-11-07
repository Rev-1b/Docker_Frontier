from django.db import models
from Frontier.common.models import NormalStringMixin


class MainPageModel(NormalStringMixin, models.Model):
    name = models.CharField(max_length=255, default='Empty', verbose_name='Имя страницы')

    class Meta:
        verbose_name = 'Основная страница'
        verbose_name_plural = 'Основные страницы'


class ChapterModel(NormalStringMixin, models.Model):
    name = models.CharField(max_length=255, default='Empty', verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    upper_text = models.TextField(verbose_name='Вступительный текст')
    lower_text = models.TextField(verbose_name='Концовка главы')
    master_page = models.ForeignKey(MainPageModel, null=True, on_delete=models.SET_NULL, related_name='chapters',
                                    verbose_name='Главная страница')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'


class ContentBlockWithImageVideoModel(NormalStringMixin, models.Model):
    name = models.CharField(max_length=255, default='Empty', verbose_name='Имя блока')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    content = models.TextField(verbose_name='Наполнение')
    image = models.ImageField(upload_to='additional/', null=True, blank=True, verbose_name='Ссылка на изображение')
    video_link = models.CharField(max_length=255, blank=True, verbose_name='Ссылка на видео')
    image_or_video_descr = models.CharField(max_length=255, verbose_name='Описание фото/видео')
    master_chapter = models.ForeignKey(ChapterModel, null=True, on_delete=models.SET_NULL, related_name='content',
                                       verbose_name='Связанная глава')

    class Meta:
        verbose_name = 'Основная контентная единица'
        verbose_name_plural = 'Основные контентные единицы'


class AbstractTitanModel(NormalStringMixin, models.Model):
    def user_directory_path(instance, filename):
        return "{0}/{1}".format(instance.name, filename)

    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    name = models.CharField(max_length=255, default='Empty', verbose_name='Имя титана')
    mp_descr = models.TextField(blank=True, verbose_name='Описание на основной странице')
    mp_image = models.ImageField(upload_to=user_directory_path, verbose_name='Фото на основной странице')

    class Meta:
        abstract = True


class FirstGenTitanModel(AbstractTitanModel):
    master_page = models.ForeignKey(MainPageModel, null=True, on_delete=models.SET_NULL, related_name='old_titans',
                                    verbose_name='Главная страница')

    class Meta:
        verbose_name = 'Титан первого поколения'
        verbose_name_plural = 'Титаны первого поколения'


class SecondGenTitanModel(AbstractTitanModel):
    full_descr = models.TextField(blank=True, verbose_name='Подробное описание')
    video_link = models.CharField(max_length=255, blank=False, verbose_name='Ссылка на видео')
    ancestor_model = models.ForeignKey(FirstGenTitanModel, null=True, on_delete=models.SET_NULL,
                                       related_name='children', verbose_name='Модель-предок')

    class Meta:
        verbose_name = 'Титан второго поколения'
        verbose_name_plural = 'Титаны второго поколения'


class AbstractEquipmentModel(NormalStringMixin, models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    name = models.CharField(max_length=255, default='Empty', verbose_name='Название снаряжения')
    descr = models.TextField(blank=False, verbose_name='Описание снаряжения')
    master_titan = models.ForeignKey(SecondGenTitanModel, null=True, on_delete=models.SET_NULL,
                                     related_name='equipment', verbose_name='Титан-владелец')


class TitanWeaponModel(AbstractEquipmentModel):
    def user_directory_path(instance, filename):
        return "{0}/{1}".format(instance.master_titan.name, filename)

    weapon_image = models.ImageField(upload_to=user_directory_path, verbose_name='Изображение оружия')

    class Meta:
        verbose_name = 'Основное снаряжение титанов'
        verbose_name_plural = 'Основное снаряжение титанов'


class TitanKitModel(AbstractTitanModel):
    class Meta:
        verbose_name = 'Дополнительный набор титана'
        verbose_name_plural = 'Дополнительные наборы титанов'


MY_MODELS = [ContentBlockWithImageVideoModel, FirstGenTitanModel, SecondGenTitanModel,
             TitanWeaponModel, TitanKitModel]
