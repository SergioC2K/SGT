from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
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

class Perfil(BaseModel, models.Model):
    """Modelo de Perfil de Usuario"""
    telefono_regex = RegexValidator(
        regex=r'^[1-9]\d{6,9}$',
        message="El numero de telefono debe tener el siguiente formato 1234567890, "
                "sin comas ni signos de puntuacion. maximo hasta 10 caracteres. mimnimo 7 caracteres"
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    cedula = models.IntegerField(default='0')
    telefono_fijo = models.CharField(validators=[telefono_regex], max_length=15)
    celular = models.CharField(validators=[telefono_regex],max_length=15)

    # Numero de celular con el cual trabajara en el telemercadeo
    celular_telemercadeo = models.CharField(validators=[telefono_regex], max_length=15)
    conexion = models.ForeignKey(Conectado, on_delete=models.PROTECT, null=True)
    foto = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    def str(self):
        """Return username"""
        return self.usuario.username

