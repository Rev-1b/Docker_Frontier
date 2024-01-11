from django.views.generic import TemplateView, DetailView
from titans.models import SecondGenTitanModel, FirstGenTitanModel, ChapterModel, MonarchCoreStageModel


class IndexView(TemplateView):
    template_name = 'titans/index.html'
    extra_context = {'title': 'TF2: Main Page'}


class TitansView(TemplateView):
    template_name = 'titans/titans.html'
    extra_context = {'title': 'TF2: Титаны', 'show_content': True}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['old_titans'] = FirstGenTitanModel.objects.all()

        context['chapters'] = ChapterModel.objects.filter(curr_page=ChapterModel.ChapterType.TITAN_PAGE)
        return context


class TitanModelView(DetailView):
    model = SecondGenTitanModel
    template_name = 'titans/titan-model.html'
    slug_url_kwarg = 'titan_slug'
    context_object_name = 'titan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'TF2: ' + context['titan'].name
        context['core_stages'] = MonarchCoreStageModel.objects.all()
        context['show_content'] = True
        return context
