from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from fourth_umpire.predictions.pred import *


from .forms import *
from .models import *

# Create your views here.
def prematch(request):
    if request.method == 'POST':
        title_form = PreMatch(request.POST)
        if title_form.is_valid():
            team1 = title_form.cleaned_data['team1']
            team2 = title_form.cleaned_data['team2']
            venue = title_form.cleaned_data['venue']
            probab = pre_match_predict("2016",team1,team2,venue)
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
