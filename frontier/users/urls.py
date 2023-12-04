from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('password-change/', NewPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', NewPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', NewPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', NewPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', NewPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', NewPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
