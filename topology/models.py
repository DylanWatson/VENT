from django.db import models
import datetime

class Machine(models.Model):
    name = models.CharField(max_length=16, unique=True) #SSH-Server
    ip = models.CharField(max_length=15, unique=True) #255.255.255.255
    number_of_threats = models.IntegerField(default=0)
    threat_level = models.IntegerField(default=0) #0-4

    def __unicode__(self):
        return self.name

class Threat(models.Model):
    name = models.CharField(max_length=64)
    sattacker = models.CharField(max_length=15, unique=True) #255.255.255.255
    reciever = models.ForeignKey(Machine)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name
