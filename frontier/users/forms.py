import django.forms as forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'username',
            'placeholder': 'Username'
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'first_name',
            'placeholder': 'First Name'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'last_name',
            'placeholder': 'Last Name'
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
            'placeholder': 'Password'
        }
    ))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Repeat Password'
        }
    ))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
