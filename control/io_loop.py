import logging
from control.models import Switches
from control.models import Lights
from control.models import LightStatus
from control.models import LightHistory
from control.models import SwitchBindings
from bbio import *
#import io

digital = []
button_list = Switches.objects.all()
light_list = Lights.objects.all()
def setup():
    for but in button_list:
        digital.append((but.pin,but))
        print(but.pin)
        print(digital)
        #pinMode(but.pin, INPUT)

    for light in light_list:
        #pinMode(light.pin, OUTPUT)
        print "hi"
def loop():
    for inputd, buttons in digital:
        if str(digitalRead(inputd)) == 'True':
            if buttons.lockable == True:
                lightstatus = LightStatus.objects.get(id=buttons.getLightID())
                lightstatus.status = True
                lightstatus.save()
                lightdetails = Lights.objects.get(id=buttons.getLightID())
                #digitalWrite(lightdetails.pin, True)
            else:
                lightstatus = LightStatus.objects.get(id=buttons.getLightID())
                lightstatus.status = False
                lightstatus.save()
                lightdetails = Lights.objects.get(id=buttons.getLightID())
                #digitalWrite(lightdetails.pin, True)
        else:
            print "button not pressed"

            #run(setup, loop)