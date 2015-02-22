from django.db import models
import datetime

class Machine(models.Model):
    ip = models.CharField(max_length=15, unique=True) #255.255.255.255
    name = models.CharField(max_length=16, default="") #SSH-Server
    number_of_threats = models.IntegerField(default=0)

    def __unicode__(self):
        return self.ip

class Threat(models.Model):
    name = models.CharField(max_length=64)
    attacker = models.CharField(max_length=15) #255.255.255.255
    reciever = models.ForeignKey(Machine, to_field='ip')
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name
