from django.views.generic import TemplateView, DetailView
from Frontier.common.views import TitleOffcanvasMixin
from titans.models import SecondGenTitanModel, FirstGenTitanModel, ChapterModel, MonarchCoreStageModel


class IndexView(TitleOffcanvasMixin, TemplateView):
    template_name = 'titans/index.html'
    title = 'TF2: Main Page'
    show_offcanvas = False


class TitansView(TitleOffcanvasMixin, TemplateView):
    template_name = 'titans/titans.html'
    title = 'TF2: Титаны'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = ChapterModel.objects.filter(curr_page=ChapterModel.ChapterType.TITAN_PAGE)
        context['old_titans'] = FirstGenTitanModel.objects.all()
        return context


class TitanModelView(TitleOffcanvasMixin, DetailView):
    model = SecondGenTitanModel
    template_name = 'titans/titan-model.html'
    slug_url_kwarg = 'titan_slug'
    context_object_name = 'titan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'TF2: ' + context['titan'].name
        context['core_stages'] = MonarchCoreStageModel.objects.all()
        return context
