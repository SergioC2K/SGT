from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tablib import Dataset
from file.models.archivo import LlamadasEntrantes
import pandas as pd
from django.views.generic import ListView, CreateView, UpdateView


# Create your views here.




@login_required
def upload_pandas(request):
    if request.method == 'POST':
        # archivo = request.FILES['myfile']
        # excel = archivo.read()
        leido = pd.read_excel(request.FILES['myfile'])
        hablalo = leido.iteritems
        oelo = []
        for data in leido.T.to_dict().values():
            oelo.append(LlamadasEntrantes(**data))

        LlamadasEntrantes.objects.bulk_create(oelo)
    return render(request, 'archivo/fileimport.html')


def preview_excel(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        data_final = imported_data.export('json')

    return render(request, 'archivo/fileimport.html')


class listar_archivo(ListView):
    model = LlamadasEntrantes
    template_name = 'archivo/listar_archivo.html'
