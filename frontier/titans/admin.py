from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import MainPageModel, ChapterModel, ContentBlockWithImageVideoModel, FirstGenTitanModel, \
    SecondGenTitanModel, TitanWeaponModel, TitanKitModel


@admin.register(MainPageModel)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ChapterModel)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'master_page']
    search_fields = ['name', 'master_page__name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['master_page']


@admin.register(ContentBlockWithImageVideoModel)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ['name', 'master_chapter']
    search_fields = ['name', 'master_chapter__name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['master_chapter']


@admin.register(FirstGenTitanModel)
class FirstGenTitanAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', ('mp_image', 'show_image'), 'mp_descr', 'master_page']
    list_display = ['name', 'show_image', 'master_page']
    readonly_fields = ['show_image']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['master_page']

    @admin.display(description='Изображение титана')
    def show_image(self, titan: FirstGenTitanModel):
        if titan.mp_image:
            return mark_safe(f"<img src='{titan.mp_image.url}' width=50>")
        return 'Нет изображения'


@admin.register(SecondGenTitanModel)
class SecondGenTitanAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', ('mp_image', 'show_image'), 'mp_descr', 'full_descr', 'video_link', 'strategy',
              'additional_info', 'ancestor_model']
    list_display = ['name', 'show_image', 'ancestor_model']
    list_editable = ['ancestor_model']
    readonly_fields = ['show_image']
    search_fields = ['name', 'ancestor_model__name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['ancestor_model']

    @admin.display(description='Изображение титана')
    def show_image(self, titan: SecondGenTitanModel):
        if titan.mp_image:
            return mark_safe(f"<img src='{titan.mp_image.url}' width=50>")
        return 'Нет изображения'


@admin.register(TitanWeaponModel)
class TitanWeaponAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', ('weapon_image', 'show_image'), 'weapon_type', 'descr', 'master_titan']
    list_display = ['name', 'weapon_type', 'show_image', 'master_titan']
    list_editable = ['weapon_type', 'master_titan']
    readonly_fields = ['show_image']
    search_fields = ['name', 'master_titan__name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['master_titan', 'weapon_type']

    @admin.display(description='Изображение оружия')
    def show_image(self, weapon: TitanWeaponModel):
        if weapon.weapon_image:
            return mark_safe(f"<img src='{weapon.weapon_image.url}' width=50>")
        return 'Нет изображения'


@admin.register(TitanKitModel)
class TitanKitAdmin(admin.ModelAdmin):
    list_display = ['name', 'master_titan']
    list_editable = ['master_titan']
    search_fields = ['name', 'master_titan__name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['master_titan']
