from django.db import models


class WeaponClassModel(models.Model):
    class Meta:
        verbose_name = "Класс оружия"
        verbose_name_plural = "Классы оружия"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, verbose_name="Название класса")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Слаг")
    descr = models.TextField(verbose_name="Описание класса")


class WeaponModel(models.Model):
    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружия"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, verbose_name="Название оружия")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Слаг")
    video_link = models.CharField(blank=True, verbose_name="Ссылка на видео")
    descr = models.TextField(verbose_name="Описание оружия")
    weapon_class = models.ForeignKey(to=WeaponClassModel, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='weapons', verbose_name='Класс оружия')
