from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput
from django.utils.translation import gettext_lazy as _


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        edit_only=True
        fields = ['username', 'password']
        
        labels = {
            'username': _('Nombre de usuario'),
            'password': _('Contraseña')
        }

        help_texts = {
            'username': _('')
        }

class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

        widgets = {
            'password': PasswordInput()
        }

        labels = {
            'username': _('Nombre de usuario'),
            'password': _('Contraseña'),
            'email': _('Dirección Email')
        }

        help_texts = {
            'username': _('')
        }
