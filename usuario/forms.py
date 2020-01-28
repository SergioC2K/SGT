"""Formularios de Usuario."""

# Django
from django import forms

#  Models
from django.contrib.auth.models import User
from usuario.models import Perfil, Conectado



class SignupForm(forms.Form):
    """Formulario de Registro de Usuario"""
    CARGOS = (
        (True, 'Coordinador'),
        (False, 'Operador'),
    )


    is_staff = forms.ChoiceField(label='Cargo',choices=CARGOS, widget=forms.RadioSelect)

    def clean_email(self):
        """Username sea unico"""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(username=email).exists()
        if email_taken:
            raise forms.ValidationError('Email ya se encuentra registrado.')

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
        conexion = Conectado()
        conexion.save()
        profile = Perfil(usuario=user, conexion=conexion)
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
            raise forms.ValidationError('Cedula ya se encuentra registrada.')
