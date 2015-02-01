from django.shortcuts import render
from django.http import HttpResponse
from topology.models import Machine, Threat

def index(request):
    context_dict = {}
    machine_list = Machine.objects.all()
    context_dict['machines'] = machine_list
    context_dict['top'] = 400
    context_dict['left'] = 400
    return render(request, 'topology/index.html', context_dict)
