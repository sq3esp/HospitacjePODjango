from django.shortcuts import render
from django.http import HttpResponse
from .models import ProtocolAppeal


def index(request):
    return render(request, 'hospitation_manager/index.html')

def appeal_responses_index(request):
    template = 'hospitation_manager/appeal_responses/index.html'
    context = {
        'appeals': ProtocolAppeal.objects.all()
    } 
    return render(request, template, context)

def appeal_responses_details(request, id):
    template = 'hospitation_manager/appeal_responses/details.html'
    context = {
        'appeal': ProtocolAppeal.objects.filter(id=id)[0]
    }

    return render(request, template, context)