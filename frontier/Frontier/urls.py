from django.contrib import admin
from django.urls import path
from titans.views import IndexView, TitansView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('titans/', TitansView.as_view(), name='titans'),
]
