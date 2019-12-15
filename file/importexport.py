from import_export import resources
from file.models import LlamadasEntrantes
from import_export.fields import Field


class PersonResource(resources.ModelResource):

    class Meta:
        model = LlamadasEntrantes
