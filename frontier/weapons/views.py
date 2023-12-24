from django.views.generic import ListView

from weapons.models import *
from titans.models import ChapterModel


class MainWeaponPageView(ListView):
    model = WeaponClassModel
    template_name = 'weapons/weapons-main-page.html'
    context_object_name = 'categories'
    extra_context = {'title': 'TF2: Вооружение', 'show_content': True,
                     'chapters': ChapterModel.objects.filter(curr_page=ChapterModel.ChapterType.WEAPON_PAGE)}

