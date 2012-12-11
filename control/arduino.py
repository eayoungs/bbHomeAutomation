
import logging
from control.models import Switches
from control.models import SwitchBindings


PORT = '/dev/ttyACM0'
board = pyfirmata.Arduino(PORT)
digital = []
button_list = Switches.objects.all()

#for but in button_list:
#	digital.append(((board.get_pin('d:' + str(but.pin) + ':i'),but)))
#	print(but.pin)
#	print(digital)


#it = pyfirmata.util.Iterator(board)
#it.start()

#for inputd, buttons in digital:
#	inputd.enable_reporting()
	
class refresh_loop:
	def loop():
		# print "looping"
# 		for inputd, buttons in digital:
# 			if str(inputd.read()) == 'True':
# 				
# 				print "Button pressed"
# 				if buttons.lockable == True:
# 					lightstatus = LightStatus.objects.get(id=buttons.getLightID())
# 					lightstatus.status = True
# 					lightstatus.save()
# 					lightdetails = Lights.objects.get(id=buttons.getLightID())
# 					board.digital[lightdetails.pin].write(1)
# 				else:
# 					lightstatus = LightStatus.objects.get(id=buttons.getLightID())
# 					lightstatus.status = False
# 					lightstatus.save()
# 					lightdetails = Lights.objects.get(id=buttons.getLightID())
# 					board.digital[lightdetails.pin].write(0)
# 			elif str(inputd.read()) == 'False':
				print "button not pressed"
