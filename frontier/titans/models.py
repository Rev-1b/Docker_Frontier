from django.db import models


class MainPageModel(models.Model):
    """
    Probably will be implemented later
    """
    pass


class AbstractTitanModel(models.Model):
    def user_directory_path(instance, filename):
        return "{0}/{1}".format(instance.titan_name, filename)

    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    titan_name = models.CharField(max_length=255, null=False)
    mp_descr = models.TextField(blank=True)
    mp_image = models.ImageField(upload_to=user_directory_path)

    class Meta:
        abstract = True


class FirstGenTitanModel(AbstractTitanModel):
    pass


class SecondGenTitanModel(AbstractTitanModel):
    full_descr = models.TextField(blank=True)
    video_link = models.CharField(max_length=255, blank=False)
    ancestor_model = models.ForeignKey(FirstGenTitanModel, null=True, on_delete=models.SET_NULL)


class AbstractEquipmentModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    equipment_name = models.CharField(max_length=255, null=False)
    descr = models.TextField(blank=False)
    master_titan = models.ForeignKey(SecondGenTitanModel, null=True, on_delete=models.SET_NULL)


class TitanWeaponModel(AbstractEquipmentModel):
    def user_directory_path(instance, filename):
        return "{0}/{1}".format(instance.master_titan.titan_name, filename)

    weapon_image = models.ImageField(upload_to=user_directory_path)


class TitanKitModel(AbstractTitanModel):
    pass

