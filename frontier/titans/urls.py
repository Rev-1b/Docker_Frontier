from django.urls import path
from titans.views import TitansView, IonView

urlpatterns = [
    path('', TitansView.as_view(), name='titans'),
    path('ion/', IonView.as_view(), name='ion'),
]
