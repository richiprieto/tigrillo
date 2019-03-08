from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Ciclo
from .models import Profesiones
from .models import Repeticion

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

def index(request):
    var= Ciclo.objects.all().order_by('ciclo_text')
    prof= Profesiones.objects.all().order_by('prof_text')
    rep= Repeticion.objects.all().order_by('repeticion_text')

    return  render(request, 'carrera_list.html',{'ciclo':var, 'profe':prof, 'rept':rep})


#def index(request):
#    z = [1, 2, 3, 4]
#    return  render(request, 'carrera_list.html', {'z': z})
