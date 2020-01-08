"""Django Utilidades para el Modelo"""

from django.db import models


class BaseModel(models.Model):
    """
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Fecha-Hora en que se creo.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Fecha y hora en que se modificó el objeto por última vez.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']