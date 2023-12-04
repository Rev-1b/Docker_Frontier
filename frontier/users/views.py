from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserLoginForm, CreateUserForm, UserProfileForm, NewPasswordChangeForm


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('index')


class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация'}

    def get_success_url(self):
        return reverse_lazy('users:login')


class ProfileUserView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль'}

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:profile')


class NewPasswordChangeView(PasswordChangeView):
    form_class = NewPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change.html'
    extra_context = {'title': 'Изменение пароля'}


class NewPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class NewPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class NewPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class NewPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class NewPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
