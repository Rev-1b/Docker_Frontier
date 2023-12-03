from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import UserLoginView, CreateUserView, ProfileUserView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
]
