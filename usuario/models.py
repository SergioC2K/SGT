from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)


    cedula = models.IntegerField(unique=True)

    telefono_fijo = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)

    # Numero de celular con el cual trabajara en el telemercadeo
    celular_telemercadeo = models.CharField(max_length=20)

    cargo = models.CharField(max_length=10, null='false')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def str(self):
        """Return username"""

        return self.usuario.username
