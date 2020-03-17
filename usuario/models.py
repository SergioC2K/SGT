from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from utils.models import BaseModel


class Conectado(BaseModel, models.Model):
    ESTADOS = [
        (True, 'Conectado'),
        (False, 'No Conectado')
    ]

    estado = models.BooleanField(
        choices=ESTADOS,
        default=False
    )

    def __str__(self):
        return str(self.estado)

class Perfil(BaseModel, models.Model):
    """Modelo de Perfil de Usuario"""

    telefono_regex = RegexValidator(
        regex=r'^[1-9]\d{6,9}$',
        message="El numero de telefono debe tener el siguiente formato 1234567890, "
                "sin comas ni signos de puntuacion. maximo hasta 10 caracteres. mimnimo 7 caracteres"
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    cedula = models.PositiveIntegerField(default='0')
    telefono_fijo = models.CharField(validators=[telefono_regex], max_length=15)
    celular = models.CharField(validators=[telefono_regex], max_length=15)

    # Numero de celular con el cual trabajara en el telemercadeo
    celular_telemercadeo = models.CharField(validators=[telefono_regex], max_length=15)
    conexion = models.ForeignKey(Conectado, on_delete=models.PROTECT, null=True)
    foto = models.ImageField(
        upload_to="media",
        blank=True,

    )

    def __str__(self):
        """Return username"""
        return self.usuario.username


from django.db.models.signals import post_save
from notifications.signals import notify


def my_handler(sender, instance, created, **kwargs):
    alo = 1
    alo = 1
    notify.send(Perfil, recipient=User.objects.filter(is_staff=True), verb='you re level 10')


post_save.connect(my_handler, sender=Perfil)