from django.contrib import admin
from django.urls import path, include
from titans.views import IndexView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('titans/', include('titans.urls')),
    path('pilots/', include('pilots.urls')),
    path('weapons/', include('weapons.urls')),
    path('users/', include('users.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Управление сайтом TitanFun2'
admin.site.index_title = 'Администрирование Базы Данных'