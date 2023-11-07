from django.contrib import admin
from .models import MY_MODELS, MainPageModel, ChapterModel, ContentBlockWithImageVideoModel, FirstGenTitanModel, \
    SecondGenTitanModel, TitanWeaponModel, TitanKitModel

for model in MY_MODELS:
    admin.site.register(model)


@admin.register(MainPageModel)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    # @admin.display(description='Количество глав')
    # def get_amount(self, page: MainPageModel):
    #     return f'{sum(page.chapters)}'


@admin.register(ChapterModel)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ['name', 'master_page']
    search_fields = ['name', 'master_page__name']
    list_filter = ['master_page']

