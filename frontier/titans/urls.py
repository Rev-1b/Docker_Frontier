from django.urls import path
from titans.views import TitansView, TitanModelView

urlpatterns = [
    path('', TitansView.as_view(), name='titans'),
    path('<slug:titan_slug>', TitanModelView.as_view(), name='titan_model'),
]
