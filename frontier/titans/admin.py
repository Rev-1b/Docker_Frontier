from django.contrib import admin
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
    list_display = ['name', 'master_page']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['master_page']


@admin.register(SecondGenTitanModel)
class SecondGenTitanAdmin(admin.ModelAdmin):
    list_display = ['name', 'ancestor_model']
    search_fields = ['name', 'ancestor_model__name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['ancestor_model']


@admin.register(TitanWeaponModel)
class TitanWeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'master_titan']
    search_fields = ['name', 'master_titan__name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['master_titan']


@admin.register(TitanKitModel)
class TitanKitAdmin(admin.ModelAdmin):
    list_display = ['name', 'master_titan']
    search_fields = ['name', 'master_titan__name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['master_titan']
