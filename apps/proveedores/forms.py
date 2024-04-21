from django import forms
from .models import Proveedor


class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
