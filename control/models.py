from django.db import models
from django.contrib import admin

class Pins(models.Model):
    headerchoice = (('P8','P8'), ('P9', 'P9'))
    id = models.AutoField(primary_key=True)
    pin = models.CharField(max_length=128)
    pinnum = models.CharField(max_length=128)
    pinheader = models.CharField(max_length=2, choices=headerchoice)

    def __unicode__(self):
        return self.pin

class Lights(models.Model):
    id = models.AutoField(primary_key=True)
    pin = models.OneToOneField(Pins)
    description = models.TextField()
    location = models.TextField()
    lockable = models.BooleanField()
    #image = models.ImageField(upload_to='/images')

    def getLightStatus(self):
        lightst = LightStatus.objects.get(id=self.id)
        return lightst.status
        lightst = property(Lights.getLightStatus())

    def getLastChanged(self):
        lightch = LightStatus.objects.get(id=self.id)
        return lightch.last_changed
        lightcha = property(Lights.getLastChanged())

    def __unicode__(self):
        return self.description


class SwitchBindings(models.Model):
    id = models.AutoField(primary_key=True)
    #switch = models.OneToOneField(Switches)
    light = models.OneToOneField(Lights)

    def __unicode__(self):
        return self.light.description

    def getLightID(self):
        return self.light.id
        lightid = property(SwitchBindings.getLightID())


class Switches(models.Model):
    id = models.AutoField(primary_key=True)
    pin = models.OneToOneField(Pins)
    description = models.TextField()
    location = models.TextField()
    setto = models.BooleanField()
    binding = models.ForeignKey(SwitchBindings)

    def __unicode__(self):
        return self.description

    def getLightID(self):
        lightdetails = SwitchBindings.objects.get(self)
        return lightdetails.light.id
    #simage = models.ImageField(upload_to='/images')


class LightStatus(models.Model):
    id = models.AutoField(primary_key=True)
    light = models.ForeignKey('Lights')
    status = models.BooleanField()
    last_changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.light.description

    # Create your models here.
class LightHistory(models.Model):
    id = models.AutoField(primary_key=True)
    light = models.ForeignKey('Lights')
    tostatus = models.BooleanField()
    timestamp = models.DateTimeField(auto_now=True)
    userid = models.IntegerField()
    method = models.IntegerField() #1 = button, 2 = web

    def __unicode__(self):
        return self.id