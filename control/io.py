import logging
from control.models import Switches
from control.models import Lights
from control.models import LightStatus
from control.models import LightHistory
from control.models import SwitchBindings
#from bbio import *

#SET OUTPUTS
def set(pid, status):
    if status == True:
        lightstatus = LightStatus.objects.get(id=pid)
        lightstatus.status = True
        lightstatus.save()
        lightdetails = Lights.objects.get(id=pid)
        #digitalWrite(lightdetails.pin, True)
    else:
        lightstatus = LightStatus.objects.get(id=pid)
        lightstatus.status = False
        lightstatus.save()
        lightdetails = Lights.objects.get(id=pid)
        #digitalWrite(lightdetails.pin, True)

def setPin(pin, status):
    if status == True:
        lightdetails = Lights.objects.get(pin=pid)
        lightstatus = LightStatus.objects.get(id=lightdetails.id)
        lightstatus.status = True
        lightstatus.save()
        #digitalWrite(pin, True)
    else:
        lightstatus = LightStatus.objects.get(id=pid)
        lightstatus.status = False
        lightstatus.save()
        lightdetails = Lights.objects.get(id=pid)
        #digitalWrite(pin, True)