from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
        labels = {
            'username': _('Nombre de usuario'),
            'password': _('Contraseña')
        }

        help_texts = {
            'username': _('')
        }

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label=_('Contraseña'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'required':'true'}))
    password2 = forms.CharField(label=_('Confirmar contraseña'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'required':'true'}))
    def __init__(self, *args, **kwargs) -> None:
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        labels={
            'username': _('Nombre de usuario')
        }