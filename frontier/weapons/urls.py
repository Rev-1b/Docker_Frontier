from django.urls import path
from weapons.views import *

urlpatterns = [
    path('', MainWeaponPageView.as_view(), name='weapons-main-page')
]