from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    """Modelo de Perfil de Usuario"""

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    cedula = models.IntegerField(default='0')
    telefono_fijo = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)

    # Numero de celular con el cual trabajara en el telemercadeo
    celular_telemercadeo = models.CharField(max_length=20)

    foto = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def str(self):
        """Return username"""

        return self.usuario.username
