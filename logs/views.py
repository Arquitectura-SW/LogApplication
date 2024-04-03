from django.shortcuts import render
from django.contrib import messages
from .forms import solicitudForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_logs import getLogs, createLog

def logsList(request):
    listaSol = getLogs()
    context = {
        'logsList':listaSol
    }
    return render(request, 'logs/logs.html', context)

def postLog(request):
    if request.method == 'POST':
        form = solicitudForm(request.POST)
        if form.is_valid():
            createLog(form)
            messages.add_message(request, messages.SUCCESS, 'log created successful')
            return HttpResponseRedirect(reverse('createLog'))
        else:
            print(form.errors)
    else:
        form = solicitudForm()

    context = {
        'form': form,
    }

    return render(request, 'logs/createdlogs.html', context)

