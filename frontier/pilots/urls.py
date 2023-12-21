from django.urls import path
from pilots.views import *

urlpatterns = [
    path('', PilotsMainPageView.as_view(), name='pilots'),
    path('<slug:pilot_slug>', PilotTacticalView.as_view(), name='tactical'),
]