"""Formularios de Usuario."""

# Django
from django import forms

#  Models
from django.contrib.auth.models import User
from usuario.models import Perfil

#class SignupForm(forms.Form):
#    """Sign up form."""
#
#    username = forms.CharField(min_length=4, max_length=50)
#
#    password = forms.CharField(
#        max_length=70,
#        widget=forms.PasswordInput()
#    )
#    password_confirmation = forms.CharField(
#        max_length=70,
#        widget=forms.PasswordInput()
#    )
#
#    first_name = forms.CharField(min_length=2, max_length=50)
#    last_name = forms.CharField(min_length=2, max_length=50)
#
#    email = forms.CharField(
#        min_length=6,
#        max_length=70,
#        widget=forms.EmailInput()
#    )
#
#    def clean_username(self):
#        """Username must be unique."""
#        username = self.cleaned_data['username']
#        username_taken = User.objects.filter(username=username).exists()
#        if username_taken:
#            raise forms.ValidationError('Username is already in use.')
#        return username
#
#    def clean(self):
#        """Verify password confirmation match."""
#        data = super().clean()
#
#        password = data['password']
#        password_confirmation = data['password_confirmation']
#
#        if password != password_confirmation:
#            raise forms.ValidationError('Passwords do not match.')
#
#        return data
#
#    def save(self):
#        """Create user and profile."""
#        data = self.cleaned_data
#        data.pop('password_confirmation')
#
#        user = User.objects.create_user(**data)
#        profile = Profile(user=user)
#        profile.save()


class SignupForm(forms.Form):
    """Formulario de Registro de Usuario"""
    CARGOS = (
        (True, 'Coordinador'),
        (False, 'Operador'),
    )
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
    is_staff = forms.ChoiceField(choices=CARGOS, widget=forms.RadioSelect)

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
        profile = Perfil(usuario=user)
        profile.save()


class PerfilForm(forms.ModelForm):
    """Formulario de Perfil"""
    class Meta:
        model = Perfil
        fields = '__all__'

    def clean(self):
        """Verificar cedula unica"""
        cedula = self.cleaned_data['cedula']
        cedula_query = Perfil.objects.filter(cedula=cedula).exists()
        if cedula_query:
            raise forms.ValidationError('Usuario ya se encuentra registrado.')
