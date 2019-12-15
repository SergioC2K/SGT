"""Formularios de Usuario."""

# Django
from django import forms

#  Models
from django.contrib.auth.models import User
from usuario.models import Perfil


class SignupForm(forms.Form):
    """Formulario de Registro de Usuario"""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    is_staff = forms.BooleanField()
    cedula = forms.IntegerField()
    telefono_celular = forms.CharField(max_length=10, min_length=7)

    # telefono_fijo = telefono_fijo,
    # celular = celular,
    # celular_telemercadeo = celular_telemercadeo,

    def clean_cedula(self):
        """Cedula sea unica"""
        cedula = self.cleaned_data['cedula']
        cedula_limpia = Perfil.objects.filter(cedula=cedula).exists()
        if cedula_limpia:
            raise forms.ValidationError('Cedula ya se encuentra registrada.')

    def clean_email(self):
        """Email sea unico"""
        email = self.cleaned_data['email']
        email_limpio = User.objects.filter(email=email).exists()
        if email_limpio:
            raise forms.ValidationError('Email ya se encuentra registrado')

        return email

    def clean_username(self):
        """Username sea unico"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Usuario ya se encuentra registrado.')

        return username

    def clean(self):
        """Verify password confirmation"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Contraseñas diferentes')

        return data

    def save(self):
        """Creando usuario y pefil"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)  # Aqui estamos desplegando el objeto completo
        profile = Perfil(user=user)
        profile.save()


class PerfilForm(forms.Form):
    cedula = forms.IntegerField(min_value=8, required=True)
    celular = forms.CharField(max_length=20)
    celular_telemercadeo = forms.CharField(max_length=20)
    nombre = forms.CharField(min_length=2, max_length=50)
    apellido = forms.CharField(min_length=2, max_length=50)
    telefono_fijo = forms.CharField(max_length=20)
    password = forms.CharField(max_length=128)
