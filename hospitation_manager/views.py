from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ProtocolAppeal, AcademicTeacher


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



def wzhz_index(request):
    template = 'hospitation_manager/wzhz/index.html'
    wzhz_members = AcademicTeacher.objects.filter(belongs_to_WZHZ=True)
    context = {'wzhz_members': wzhz_members}
    return render(request, template, context)

def wzhz_add(request):
    template = 'hospitation_manager/wzhz/add.html'
    context = {}
    return render(request, template, context)

def wzhz_details(request, wzhz_id):
    wzhz_member = get_object_or_404(AcademicTeacher, pk=wzhz_id)
    context = {
        'wzhz_member': wzhz_member,
    }
    return render(request, 'hospitation_manager/wzhz/details.html', context)
