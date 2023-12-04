from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import UserLoginView, CreateUserView, ProfileUserView, NewPasswordChangeView, NewPasswordChangeDoneView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('password_change/', NewPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', NewPasswordChangeDoneView.as_view(), name='password_change_done'),

]
