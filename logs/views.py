from django.shortcuts import render
from django.contrib import messages
from .forms import solicitudForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_logs import getLogs, createLog, getLogsByDocumento

def logsList(request):
    listaSol = getLogs()
    context = {
        'logsList':listaSol
    }
    return render(request, 'logs/logs.html', context)

def logsListDocumento(request, documento):
    listaSol = getLogsByDocumento(documento)
    context = {
        'logsList':listaSol
    }
    return render(request, 'logs/logsByDoc.html', context)

