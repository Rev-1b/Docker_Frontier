from django.contrib import admin
from django.urls import path, include
from titans.views import IndexView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('titans/', include('titans.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
