from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.views import login
from control.models import Lights
from control.models import Switches
from control.models import LightStatus
from control.models import SwitchBindings
from control.models import LightHistory
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

import io

def index(request):
    light_list = Lights.objects.all().order_by('id')
    return render_to_response('lights/index.html', {'lightlist': light_list})


def light(request, light_id):
    try:
        lightdetails = Lights.objects.get(id=light_id)
    except Lights.DoesNotExist:
        raise Http404
    light_list = Lights.objects.all().order_by('id')
    randomnum = User.objects.make_random_password(length=10, allowed_chars='123456789')
    return render_to_response('lights/light.html', {'light': lightdetails, 'lightlist': light_list, 'rand': randomnum})


def lighton(request, light_id):
    try:
        lightstatus = LightStatus.objects.get(id=light_id)
        lightstatus.status = True
        lightstatus.save()
        lightdetails = Lights.objects.get(id=light_id)
        b = LightHistory(light=lightdetails, tostatus=True, userid='0', method='1')
        b.save()
    except LightStatus.DoesNotExist:
        raise Http404
    lightdetails = Lights.objects.get(id=light_id)
    lightstatus = LightStatus.objects.get(id=light_id)
    print lightdetails.pin
    io.set(light_id, True)
    light_list = Lights.objects.all().order_by('id')
    randomnum = User.objects.make_random_password(length=10, allowed_chars='123456789')
    return render_to_response('lights/light.html',
        {'light': lightdetails, 'status': lightstatus, 'lightlist': light_list, 'rand': randomnum})


def lightoff(request, light_id):
    try:
        lightstatus = LightStatus.objects.get(id=light_id)
        lightstatus.status = False
        lightstatus.save()
        lightdetails = Lights.objects.get(id=light_id)
        b = LightHistory(light=lightdetails, tostatus=False, userid='0', method='1')
        b.save()
    except LightStatus.DoesNotExist:
        raise Http404
    lightdetails = Lights.objects.get(id=light_id)
    lightstatus = LightStatus.objects.get(id=light_id)
    io.set(light_id, False)
    light_list = Lights.objects.all().order_by('id')
    randomnum = User.objects.make_random_password(length=10, allowed_chars='123456789')
    return render_to_response('lights/light.html',
        {'light': lightdetails, 'status': lightstatus, 'lightlist': light_list, 'rand': randomnum})


def lighthistory(request, light_id):
    try:
        lightdetails = Lights.objects.get(id=light_id)
        lighthistory = LightHistory.objects.all().order_by('timestamp')
        lighthistory = LightHistory.objects.filter(light=lightdetails)
    except Lights.DoesNotExist:
        raise Http404
    light_list = Lights.objects.all().order_by('id')
    return render_to_response('lights/lighthistory.html',
        {'light': lightdetails, 'history': lighthistory, 'lightlist': light_list})


def button(request, btn_id):
    buttons = Switches.objects.get(pin=btn_id)
    if buttons:
        buttonbind = buttons.binding
        lid = buttonbind.light.id
        lightdetails = buttonbind.light
        if buttons.lockable == True:
            lightstatus = LightStatus.objects.get(id=lid)
            lightstatus.status = True
            lightstatus.save()
            io.set(lightdetails.id, True)
        else:
            lightstatus = LightStatus.objects.get(id=lid)
            lightstatus.status = True
            lightstatus.save()
            io.set(lightdetails.id, False)
    return HttpResponse("1")

def allon(request):
    try:
        lights_list = Lights.objects.all().order_by('id')
        for light in lights_list:
            lightstatus = LightStatus.objects.get(id=light.id)
            lightstatus.status = True
            lightstatus.save()
            b = LightHistory(light=light, tostatus=True, userid='0', method='1')
            b.save()
            #io.setpin(light.pin, True) -- re-enable once on BB

    except LightStatus.DoesNotExist:
        raise Http404

    light_list = Lights.objects.all().order_by('id')
    randomnum = User.objects.make_random_password(length=10, allowed_chars='123456789')
    return render_to_response('lights/index.html',
        {'lightlist': light_list, 'rand': randomnum, 'all': '1'})
def alloff(request):

    try:
        lights_list = Lights.objects.all().order_by('id')
        for light in lights_list:
            lightstatus = LightStatus.objects.get(id=light.id)
            lightstatus.status = False
            lightstatus.save()
            b = LightHistory(light=light, tostatus=False, userid='0', method='1')
            b.save()
            #io.setpin(light.pin, False) -- re-enable once on BB

    except LightStatus.DoesNotExist:
        raise Http404

    light_list = Lights.objects.all().order_by('id')
    randomnum = User.objects.make_random_password(length=10, allowed_chars='123456789')
    return render_to_response('lights/index.html',
        {'lightlist': light_list, 'rand': randomnum, 'all': '2'})