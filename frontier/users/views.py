from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, TemplateView

from users.forms import *
from users.models import EmailVerificationModel


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


class ProfileUserView(LoginRequiredMixin, View):
    def get(self, request):
        main_form = UserProfileMainForm(instance=request.user)
        sub_form = UserProfileSubForm(instance=request.user.profile)

        context = {
            'title': 'Профиль',
            'main_form': main_form,
            'sub_form': sub_form,
        }

        return render(request, 'users/profile.html', context=context)

    def post(self, request):
        main_form = UserProfileMainForm(request.POST, instance=request.user)
        sub_form = UserProfileSubForm(request.POST, instance=request.user.profile)
        if main_form.is_valid() and sub_form.is_valid():
            main_form.save()
            sub_form.save()

            context = {
                'title': 'Профиль',
                'main_form': main_form,
                'sub_form': sub_form,
            }

            return render(request, 'users/profile.html', context=context)

        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')


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
    form_class = NewSetPasswordForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class NewPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class EmailVerificationView(TemplateView):
    extra_context = {'title': 'E-mail подтвержден'}
    template_name = 'users/verified_email.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = get_user_model().objects.get(email=kwargs['email'])
        email_verifications = EmailVerificationModel.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.profile.is_email_verified = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))