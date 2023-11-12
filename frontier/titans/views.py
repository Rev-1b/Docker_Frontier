from django.views.generic import TemplateView, DetailView
from Frontier.common.views import TitleMixin
from titans.models import SecondGenTitanModel, FirstGenTitanModel, ChapterModel


class IndexView(TitleMixin, TemplateView):
    template_name = 'titans/index.html'
    title = 'TF2: Main Page'


class TitansView(TemplateView):
    template_name = 'titans/titans.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TF2: Титаны'
        context['chapters'] = ChapterModel.objects.filter(master_page__name='Титаны')
        context['old_titans'] = FirstGenTitanModel.objects.all()
        return context


class TitanModelView(DetailView):
    model = SecondGenTitanModel
    template_name = 'titans/titan-model.html'
    slug_url_kwarg = 'titan_slug'
    context_object_name = 'titan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'TF2: ' + context['titan'].name
        return context
