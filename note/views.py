# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from note.models import Cotisant
from django.http import HttpResponse
from django.template import Template
from .forms import NameForm
import os.path, time


def get_note(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():           
            # process the data in form.cleaned_data as required
            try:
                gold = "Ta note de fouaille est %s € " %  Cotisant.objects.get(numero_carte__exact=form.cleaned_data['your_name']).note
            except:
                gold = "Carte inconnue"
            return render(request, 'result.html',locals())

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        # On récupère la date de modification du dernier backup 
        temps =" Mis à jour le %s " % time.strftime('%d/%m/%Y à %H:%M', time.gmtime(os.path.getmtime("/home/bde/last_backup.sql")))
    return render(request, 'note.html', locals())
    
