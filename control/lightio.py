import logging
from control.models import Switches
from control.models import Lights
from control.models import LightStatus
from control.models import Pins
from control.models import LightHistory
from control.models import SwitchBindings
#from bbio import *
#SET OUTPUTS

digital = []
button_list = Switches.objects.all()
light_list = Lights.objects.all()


def setup():
    for light in light_list:
        #pinMode(light.pin.pin, OUTPUT)
        print "hi"



def set(pid, status):
    if status == True:
        lightstatus = LightStatus.objects.get(id=pid)
        lightstatus.status = True
        lightstatus.save()
        lightdetails = Lights.objects.get(id=pid)
        #digitalWrite(lightdetails.pin.pin, True)
    else:
        lightstatus = LightStatus.objects.get(id=pid)
        lightstatus.status = False
        lightstatus.save()
        lightdetails = Lights.objects.get(id=pid)
        #digitalWrite(lightdetails.pin.pin, True)

def setPin(pinset, status):
    if status == True:
        getpin = Pins.objects.get(pin=pinset)
        lightdetails = Lights.objects.get(pin=getpin)
        lightstatus = LightStatus.objects.get(id=lightdetails.id)
        lightstatus.status = True
        lightstatus.save()
        #digitalWrite(pin, True)
    else:
        getpin = Pins.objects.get(pin=pinset)
        lightdetails = Lights.objects.get(pin=getpin)
        lightstatus = LightStatus.objects.get(id=lightdetails.id)
        lightstatus.status = False
        lightstatus.save()
        #digitalWrite(pin, False)