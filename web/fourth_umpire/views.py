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

import logging
import logging.config
from django.contrib import messages

# Create your views here.
def prematch(request):
    if request.method == 'POST':
        title_form = PreMatch(request.POST, request.FILES)
        if title_form.is_valid():
            team1 = title_form.cleaned_data['team1']
            team2 = title_form.cleaned_data['team2']
            venue = title_form.cleaned_data['venue']
            # probab = pre_match_predict("2016",team1,team2,venue)
            probab = 0.85
            if probab > 0.5 :
                winner = get_team(team1)
                probab = probab * 100
            else:
                winner =  get_team(team2)
                probab = (1- probab) * 100

            return render(request, 'fourth_umpire/pre_pred.html', context={'form3': title_form,"winner":winner,"probab":probab})

    else:
        title_form = PreMatch()

    return render(request, 'fourth_umpire/pre_pred.html', context={'form3': title_form})

def index(request):
    return render(request, 'fourth_umpire/index.html')

def display_dataset(request):
    items = DataSet.objects.all()
    context = {
        'items': items,
        'header': 'DataSet',
    }
    return render(request, 'fourth_umpire/index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'fourth_umpire/add_new.html', {'form' : form})

def add_dataset(request):
    return add_item(request, DataSetForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'fourth_umpire/edit_item.html', {'form': form})

def edit_dataset(request, pk):
    return edit_item(request, pk, DataSet, DataSetForm)


def delete_dataset(request, pk):

    template = 'fourth_umpire/index.html'
    DataSet.objects.filter(id=pk).delete()

    items = DataSet.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read().decode('utf-8'),format='csv')
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'fourth_umpire/index.html')
