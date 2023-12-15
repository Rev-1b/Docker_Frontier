import django.forms as forms
from django.forms import FileInput

from users.tasks import send_verification_email, send_reset_mail_task
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm as PasswordResetFormCore
from users.models import Profile


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
        user = super().save(commit=True)
        send_verification_email.delay(user.id)
        return user


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
    photo = forms.ImageField(label='Выберите изображение', widget=forms.FileInput(attrs={'style': 'display: none'}))

    class Meta:
        model = Profile
        fields = ['photo']


class NewPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите старый пароль'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))


class PasswordResetForm(PasswordResetFormCore):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    def send_reset_mail(self, subject_template_name, email_template_name, context,
                        from_email, to_email, html_email_template_name=None):
        context['user'] = context['user'].id

        send_reset_mail_task.delay(subject_template_name=subject_template_name,
                                   email_template_name=email_template_name,
                                   context=context, from_email=from_email, to_email=to_email,
                                   html_email_template_name=html_email_template_name)


class NewSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
