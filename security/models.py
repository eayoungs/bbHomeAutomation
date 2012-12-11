from django.db import models

# Create your models here.

class Sensors(models.Model):
    MOTION = 'MO'
    DOOR = 'DO'
    SMOKE = 'SM'
    WINDOW = 'WI'
    SOUND = 'SO'
    OTHER = 'OT'

    sensortypes = (
        (MOTION, 'Motion Sensor'),
        (DOOR, 'Door Sensor'),
        (SMOKE, 'Smoke Detector'),
        (WINDOW, 'Window Sensor'),
        (SOUND, 'Audio Sensor'),
        (OTHER, 'Other Digital Sensor'),
        )
    id = models.AutoField(primary_key=True)
    pin = models.TextField()
    sensortype = models.CharField(max_length=2, choices=sensortypes)
    description = models.TextField()
    location = models.TextField()
    alarmtype = models.IntegerField()
    bypass = models.BooleanField()

class SensorHistory(models.Model):
    id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey('Sensors')
    timestamp = models.DateTimeField(auto_now=True)
    trip = models.IntegerField()

    def __unicode__(self):
        return self.id

class alarmstatus(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.TextField()
    starttimestamp = models.DateTimeField(auto_now=True)
    endtimestamp = models.DateTimeField(auto_now=False)
    enabled = models.BooleanField()
    triggered = models.IntegerField()
    disabledby = models.TextField()

