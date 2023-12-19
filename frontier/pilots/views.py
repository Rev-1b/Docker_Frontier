from django.views.generic import TemplateView

from titans.models import ChapterModel


class PilotsMainPage(TemplateView):
    template_name = 'pilots/pilots.html'
    extra_context = {'title': 'TF2: Пилоты', 'show_content': True}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = ChapterModel.objects.filter(curr_page=ChapterModel.ChapterType.PILOT_PAGE)
        return context
