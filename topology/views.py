from django.shortcuts import render
from django.http import HttpResponse
from topology.models import Machine, Threat

def index(request):
    context_dict = {}
    machine_list = Machine.objects.all()
    context_dict['machines'] = machine_list
    context_dict['number_of_machines'] = range(0, len(machine_list))

    return render(request, 'topology/index.html', context_dict)
