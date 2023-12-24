from django.contrib import admin
from django.utils.safestring import mark_safe

from pilots.models import *


@admin.register(PilotModel)
class PilotAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'mp_descr', ('mp_logo', 'display_logo'), 'video_link',  'short_descr', 'features']
    list_display = ['name', 'mp_descr', 'display_logo']
    readonly_fields = ['display_logo']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Дополнительное изображение')
    def display_logo(self, pilot: PilotModel):
        if pilot.mp_logo:
            return mark_safe(f"<img src='{pilot.mp_logo.url}' width=50>")
        return 'Нет изображения'


@admin.register(PilotStrategyBlockModel)
class PilotStrategyBlockAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'content', ('image', 'display_image'), 'pilot']
    list_display = ['name', 'pilot', 'display_image']
    readonly_fields = ['display_image']
    list_editable = ['pilot']
    list_filter = ['pilot']
    search_fields = ['name', 'pilot__name']
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Дополнительное изображение')
    def display_image(self, pilot_strategy: PilotStrategyBlockModel):
        if pilot_strategy.image:
            return mark_safe(f"<img src='{pilot_strategy.image.url}' width=50>")
        return 'Нет изображения'


@admin.register(CarouselImagesModel)
class CarouselImagesAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', ('image', 'display_image'), 'pilot']
    list_display = ['title', 'pilot', 'display_image']
    readonly_fields = ['display_image']
    list_editable = ['pilot']
    list_filter = ['pilot']
    search_fields = ['title', 'pilot__name']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(description='Дополнительное изображение')
    def display_image(self, carousel_image: CarouselImagesModel):
        if carousel_image.image:
            return mark_safe(f"<img src='{carousel_image.image.url}' width=50>")
        return 'Нет изображения'
