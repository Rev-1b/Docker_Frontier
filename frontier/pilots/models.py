from django.db import models
from django.urls import reverse

from Frontier.common.models import NormalStringMixin
from titans.models import AbstractContentModel


class PilotModel(NormalStringMixin, models.Model):
    class Meta:
        verbose_name = 'Пилот'
        verbose_name_plural = 'Пилоты'

    def user_directory_path(instance, filename):
        return "{0}/{1}".format(instance.name, filename)

    def get_absolute_url(self):
        return reverse('tactical', kwargs={'pilot_slug': self.slug})

    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')
    name = models.CharField(max_length=100, verbose_name='Название')
    mp_descr = models.TextField(blank=True)
    mp_logo = models.ImageField(upload_to=user_directory_path, verbose_name='Логотип')
    video_link = models.CharField(blank=True, null=True, verbose_name='Ссылка на видео')
    short_descr = models.TextField(blank=True)
    features = models.TextField(blank=True, verbose_name='Особенности')


class PilotStrategyBlockModel(AbstractContentModel):
    class Meta:
        verbose_name = 'Блок стратегии'
        verbose_name_plural = 'Блоки стратегии'

    def user_directory_path(instance, filename):
        return "{0}/strategy_pictures/{1}".format(instance.pilot.name, filename)

    image = models.ImageField(upload_to=user_directory_path, db_index=True, null=True, blank=True,
                              verbose_name='Ссылка на изображение')
    pilot = models.ForeignKey(to=PilotModel, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='strategy', verbose_name='Пилот-владелец')


class CarouselImagesModel(models.Model):
    class Meta:
        verbose_name = "Изображения для карусели"
        verbose_name_plural = "Изображение для карусели"

    def user_directory_path(instance, filename):
        return "{0}/carousel/{1}".format(instance.pilot.name, filename)

    def __str__(self):
        return f'{self.title}'

    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to=user_directory_path, db_index=True, null=True, blank=True,
                              verbose_name='Ссылка на изображение')
    pilot = models.ForeignKey(to=PilotModel, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='carousel', verbose_name='Пилот-владелец')
