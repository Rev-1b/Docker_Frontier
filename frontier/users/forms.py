import uuid
from datetime import timedelta

import django.forms as forms
from django.core.mail import send_mail
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, SetPasswordForm
from users.models import Profile, EmailVerificationModel


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'username',
            'placeholder': 'Имя пользователя'
        }
    ))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Пароль'
        }
    ))


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'username',
            'placeholder': 'Имя пользователя'
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'first_name',
            'placeholder': 'Имя'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'last_name',
            'placeholder': 'Фамилия'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'placeholder': 'E-mail'
        }
    ))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Пароль'
        }
    ))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Повтор пароля'
        }
    ))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой E-mail уже существует')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        email_verification = EmailVerificationModel.objects.create(code=uuid.uuid4,
                                                                   user=user,
                                                                   expiration_time=now() + timedelta(hours=48))


class UserProfileMainForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Имя пользователя')
    email = forms.EmailField(disabled=True, label='E-mail')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите Фамилию'}),
        }


class UserProfileSubForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'photo']

        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'Расскажите о себе'}),
        }


class NewPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите старый пароль'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))


class NewSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
