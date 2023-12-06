from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', ('photo', 'show_photo'), 'bio']
    list_display = ['user', 'show_photo']
    readonly_fields = ['show_photo']
    search_fields = ['user']

    @admin.display(description='Фотография пользователя')
    def show_photo(self, profile: Profile):
        if profile.photo:
            return mark_safe(f"<img src='{profile.photo.url}' width=50>")
        return 'Нет изображения'