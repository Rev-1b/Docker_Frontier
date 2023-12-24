from django.contrib import admin
from weapons.models import *


@admin.register(WeaponClassModel)
class WeaponClassAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'descr']
    list_display = ['name', 'descr']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(WeaponModel)
class WeaponAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'video_link', 'descr', 'weapon_class']
    list_display = ['name', 'weapon_class']
    list_editable = ['weapon_class']
    list_filter = ['weapon_class__name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

