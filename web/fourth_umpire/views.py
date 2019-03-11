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

def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "fourth_umpire/upload_csv.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("upload_csv"))
        #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("upload_csv"))

		file_data = csv_file.read().decode("utf-8")

		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		for line in lines:
			fields = line.split(",")
			data_dict = {}
			data_dict["escuela"] = fields[0]
			data_dict["edad"] = fields[1]
			data_dict["sexo"] = fields[2]
			data_dict["direccion"] = fields[3]
			try:
				form = EventsForm(data_dict)
				if form.is_valid():
					form.save()
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))
				pass

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))

	return HttpResponseRedirect(reverse("upload_csv"))
