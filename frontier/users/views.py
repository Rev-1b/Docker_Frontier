from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView

from users.forms import UserLoginForm


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'


