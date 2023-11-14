from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(ChapterModel)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'curr_page']
    list_editable = ['curr_page']
    list_filter = ['curr_page']
    search_fields = ['name', 'curr_page']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MediaContentBlockModel)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ['name', 'chapter']
    list_editable = ['chapter']
    list_filter = ['chapter']
    search_fields = ['name', 'chapter__name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FirstGenTitanModel)
class FirstGenTitanAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', ('mp_image', 'show_image'), 'mp_descr']
    list_display = ['name', 'show_image']
    readonly_fields = ['show_image']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Изображение титана')
    def show_image(self, titan: FirstGenTitanModel):
        if titan.mp_image:
            return mark_safe(f"<img src='{titan.mp_image.url}' width=50>")
        return 'Нет изображения'


@admin.register(SecondGenTitanModel)
class SecondGenTitanAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', ('mp_image', 'show_image'), 'mp_descr', 'full_descr', 'video_link', 'ancestor_model']
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
    fields = ['name', 'slug', ('weapon_image', 'show_image'), 'weapon_type', 'descr', 'titan']
    list_display = ['name', 'weapon_type', 'show_image', 'titan']
    list_editable = ['weapon_type', 'titan']
    readonly_fields = ['show_image']
    list_filter = ['titan', 'weapon_type']
    search_fields = ['name', 'titan__name']
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Изображение оружия')
    def show_image(self, weapon: TitanWeaponModel):
        if weapon.weapon_image:
            return mark_safe(f"<img src='{weapon.weapon_image.url}' width=50>")
        return 'Нет изображения'


@admin.register(TitanKitModel)
class TitanKitAdmin(admin.ModelAdmin):
    list_display = ['name', 'titan']
    list_editable = ['titan']
    list_filter = ['titan']
    search_fields = ['name', 'titan__name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(StrategyBlockModel)
class StrategyBlockAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'content', ('image', 'display_image'), 'titan']
    list_display = ['name', 'titan', 'display_image']
    readonly_fields = ['display_image']
    list_editable = ['titan']
    list_filter = ['titan']
    search_fields = ['name', 'titan__name']
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Дополнительное изображение')
    def display_image(self, strategy: StrategyBlockModel):
        if strategy.image:
            return mark_safe(f"<img src='{strategy.image.url}' width=50>")
        return 'Нет изображения'


@admin.register(MonarchCoreStageModel)
class MonarchCoreStageAdmin(admin.ModelAdmin):
    list_display = ['stage']
    search_fields = ['stage']
    prepopulated_fields = {'slug': ('stage',)}


@admin.register(MonarchCoreUpgradeModel)
class MonarchCoreUpgradeAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'content', ('image', 'display_image'), 'stage']
    list_display = ['name', 'stage', 'display_image']
    readonly_fields = ['display_image']
    list_editable = ['stage']
    list_filter = ['stage']
    search_fields = ['name', 'stage__stage']
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Дополнительное изображение')
    def display_image(self, core_upgrade: MonarchCoreUpgradeModel):
        if core_upgrade.image:
            return mark_safe(f"<img src='{core_upgrade.image.url}' width=50>")
        return 'Нет изображения'
