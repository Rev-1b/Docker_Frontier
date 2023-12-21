from django.views.generic import TemplateView, DetailView

from titans.models import ChapterModel
from pilots.models import PilotModel


class PilotsMainPageView(TemplateView):
    template_name = 'pilots/pilots.html'
    extra_context = {'title': 'TF2: Пилоты', 'show_content': True}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = ChapterModel.objects.filter(curr_page=ChapterModel.ChapterType.PILOT_PAGE)
        context['pilots'] = PilotModel.objects.all()
        return context


class PilotTacticalView(DetailView):
    model = PilotModel
    template_name = 'pilots/main-ability-page.html'
    slug_url_kwarg = 'pilot_slug'
    extra_context = {'show_content': True}
    context_object_name = 'pilot'
