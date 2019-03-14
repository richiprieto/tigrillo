from tablib import Dataset

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from fourth_umpire.predictions.pred import *

from .forms import *
from .models import *

import pandas_highcharts.core

# Create your views here.
def prematch(request):
    if request.method == 'POST':
        title_form = PreMatch(request.POST, request.FILES)
        if title_form.is_valid():
            carrera = title_form.cleaned_data['carrera']
            ciclo = title_form.cleaned_data['ciclo']
            sede = title_form.cleaned_data['sede']
            document = "documents/"+str(title_form.cleaned_data['document'])
            [probab, cod_est, sexo] = pre_match_predict(document)
            winner = get_carrera(carrera)
            cod_est = pd.DataFrame(cod_est)
            #cod_est_html = cod_est.to_html()
            chart = pandas_highcharts.core.serialize(sexo, render_to='my-chart',
                                                    output_type='json',
                                                    kind = "bar",
                                                    x ="sex",
                                                    title="Distribucion general por sexo"
                                                    )
            return render(request, 'fourth_umpire/pre_pred.html', context={'form3': title_form,"winner":winner,"probab":probab,"chart":chart})

    else:
        title_form = PreMatch()

    return render(request, 'fourth_umpire/pre_pred.html', context={'form3': title_form})
