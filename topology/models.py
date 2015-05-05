from django.db import models
from django.template.defaultfilters import slugify
import datetime
from datetime import datetime

class Machine(models.Model):
    ip = models.CharField(max_length=15, unique=True) #255.255.255.255
    name = models.CharField(max_length=16, default="") #SSH-Server
    number_of_threats = models.IntegerField(default=0)
    #slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.ip

class Threat(models.Model):
    name = models.CharField(max_length=64)
    attacker = models.CharField(max_length=15) #255.255.255.255
    reciever = models.ForeignKey(Machine, to_field='ip')
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name

class Blackhole(models.Model):
    ip = models.CharField(max_length=15, unique=True) #255.255.255.255
    blackholed = models.IntegerField(default=0) #True=1 False=0
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __unicode__(self):
        return self.ip
