from django.http import HttpResponse
from django.views.generic.base import TemplateView
from Frontier.common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'titans/index.html'
    title = 'TF2: Main Page'


class TitansView(TitleMixin, TemplateView):
    template_name = 'titans/titans.html'
    title = 'TF2: Titans'


def view_function(request):
    return HttpResponse('Some response')