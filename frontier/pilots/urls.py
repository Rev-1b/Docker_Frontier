from django.urls import path
from pilots.views import *

urlpatterns = [
    path('', PilotsMainPage.as_view(), name='pilots')
]