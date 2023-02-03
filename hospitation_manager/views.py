from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from .models import ProtocolAppeal, AcademicTeacher, HospitationTeam, Hospitation
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core import serializers

import json

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
        'appeal' : get_object_or_404(ProtocolAppeal, pk=id)
    }

    return render(request, template, context)

def appeal_responses_edit(request, id):
    if request.method == 'GET':
        template = 'hospitation_manager/appeal_responses/edit.html'
        context = {
            'appeal' : get_object_or_404(ProtocolAppeal, pk=id)
        }

        return render(request, template, context)
    if request.method == 'PUT':
        data = json.load(request)
        if data.get('status') == 'accept':
            ProtocolAppeal.objects.filter(pk=id).update(status='ZA', dean_response=data.get('dean_response'))
            messages.success(request, 'Pomyślnie zaakceptowano odwołanie')
            return HttpResponse('Updated succesfully')
        if data.get('status') == 'decline':
            ProtocolAppeal.objects.filter(pk=id).update(status='OD', dean_response=data.get('dean_response'))
            messages.error(request, 'Pomyślnie odrzucono odwołanie')
            return HttpResponse('Updated succesfully')
        return HttpResponseBadRequest('Invalid request')
    return HttpResponseBadRequest('Invalid request')

def hospitation_teams_index(request):
    template = 'hospitation_manager/hospitation_teams/index.html'
    context = {
        'hospitation_teams': HospitationTeam.objects.all()
    }

    return render(request, template, context)

def hospitation_teams_details(request, id):
    template = 'hospitation_manager/hospitation_teams/details.html'
    context = {
        'team': get_object_or_404(HospitationTeam, pk=id),
        'hospitations': Hospitation.objects.filter(hospitation_team__number=id)
    }

    return render(request, template, context)

def hospitation_teams_edit(request, id):
    template = 'hospitation_manager/hospitation_teams/edit.html'
    hospitations = Hospitation.objects.filter(hospitation_team__number=id)
    all_hospitations = Hospitation.objects.all()
    context = {
        'team': get_object_or_404(HospitationTeam, pk=id),
        'hospitations': hospitations,
        'all_hospitations': all_hospitations
    }

    return render(request, template, context)

def hospitation_teams_delete(request, id):
    if request.method == 'DELETE':
        HospitationTeam.objects.get(pk=id).delete()
        return HttpResponse('Deleted succesfully')
    return HttpResponseBadRequest('Bad request')

@csrf_exempt 
def wzhz_index(request):
    message = ''
    messageColor = ''
    if request.method == 'POST':
        teacher_id = request.POST.get('id')
        if(teacher_id == None):
            return HttpResponse('Nie podano id nauczyciela')
        teacher = get_object_or_404(AcademicTeacher, pk=teacher_id)
        if(teacher == None):
            return HttpResponse('Nie znaleziono nauczyciela o podanym id')
        teacher.belongs_to_WZHZ = False
        teacher.appointment_to_WZHZ_date = None
        teacher.save()
        message = 'Nauczyciel został odwołany z komisji'
        messageColor = 'green'

    template = 'hospitation_manager/wzhz/index.html'
    wzhz_members = AcademicTeacher.objects.filter(belongs_to_WZHZ=True)
    context = {'wzhz_members': wzhz_members, 'message': message, 'messageColor': messageColor}
    return render(request, template, context)

@csrf_exempt 
def wzhz_add(request):
    message = ''
    messageColor = ''
    if request.method == 'POST':
        teacher_id = request.POST.get('id')
        if(teacher_id == None):
            return HttpResponse('Nie podano id nauczyciela')
        teacher = get_object_or_404(AcademicTeacher, pk=teacher_id)
        if(teacher == None):
            return HttpResponse('Nie znaleziono nauczyciela o podanym id')
        teacher.belongs_to_WZHZ = True
        teacher.appointment_to_WZHZ_date = datetime.today()
        teacher.save()
        message = 'Nauczyciel został dodany do WZHZ'
        messageColor = 'green'


    template = 'hospitation_manager/wzhz/add.html'
    not_wzhz_members = AcademicTeacher.objects.filter(belongs_to_WZHZ=False)
    context = {'not_wzhz_members': not_wzhz_members, 'message': message, 'messageColor': messageColor}


    return render(request, template, context)

def wzhz_details(request, wzhz_id):
    """
Shows all information about a teacher who is a member of the WZHZ
    """
    wzhz_member = get_object_or_404(AcademicTeacher, pk=wzhz_id)
    context = {
        'wzhz_member': wzhz_member,
    }
    return render(request, 'hospitation_manager/wzhz/details.html', context)

