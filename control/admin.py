from django.contrib import admin
from control.models import Lights
from control.models import Switches
from control.models import SwitchBindings
from control.models import LightStatus



class LightsAdmin(admin.ModelAdmin):
	list_display = ('description', 'id')
admin.site.register(Lights, LightsAdmin)

class SwitchesAdmin(admin.ModelAdmin):
	list_display = ('description', 'id')
admin.site.register(Switches, SwitchesAdmin)

class SwitchBindingsAdmin(admin.ModelAdmin):
	list_display = ('light', 'id')
admin.site.register(SwitchBindings, SwitchBindingsAdmin)

class LightStatusAdmin(admin.ModelAdmin):
	list_display = ('light', 'id')
admin.site.register(LightStatus, LightStatusAdmin)