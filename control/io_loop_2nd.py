__author__ = 'kyledeane'
#new, better, event based approach to button handling.
import logging
from control.models import Switches
from control.models import Lights
from control.models import LightStatus
from control.models import LightHistory
from control.models import SwitchBindings
from bbio import *
# Then we can import EventIO:
from EventIO import *


digital = []
button_list = Switches.objects.all()
light_list = Lights.objects.all()

# Create an event loop:
event_loop = EventLoop()

#--- The events to be triggered: ---
def on(lightID):
    lightdetails = Lights.objects.get(id=lightID)
    lightstatus = LightStatus.objects.get(light=lightdetails)
    lightstatus.status = True
    lightstatus.save()
    b = LightHistory(light=lightdetails, tostatus=True, userid='0', method='2')
    b.save()
    #digitalWrite(lightdetails.pin, True)

def off(lightID):
    lightdetails = Lights.objects.get(id=lightID)
    lightstatus = LightStatus.objects.get(light=lightdetails)
    lightstatus.status = False
    lightstatus.save()
    b = LightHistory(light=lightdetails, tostatus=False, userid='0', method='2')
    b.save()
    #digitalWrite(lightdetails.pin, True)

def setup():
    for but in button_list:
        digital.append((but.pin,but))
        if but.lockable:
            event_loop.add_event(DigitalTrigger(but.pin, HIGH, on(but.getLightID()), 50))
        else:
            event_loop.add_event(DigitalTrigger(but.pin, HIGH, off(but.getLightID()), 50))
    for light in light_list:
        pinMode(light.pin, OUTPUT)
        print "hi"

    # Then start the event loop:
    event_loop.start()

def loop():
    # Because the event loop is run as a seperate process, this will
    # be executed normally.
    print "Time running: %ims" % int(millis())
    delay(3000)

run(setup, loop)