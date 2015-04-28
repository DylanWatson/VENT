import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vent.settings')

import django
from vent import settings
django.setup()

from topology.models import Machine, Threat
import commands
import time

s = commands.getstatusoutput("/usr/local/bro/bin/bro-cut ts id.orig_h id.resp_h note < /usr/local/bro/logs/notice.log")
#log = [x.strip() for x in my_file.readlines
output = s[1].split("\n")
for line in output:
    attack = line.split("\t")
    date = attack[0].split(".")
    reciever = attack[1]
    attacker = attack[2]
    type_of_attack = attack[3]
    formated_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(date[0])))
    threat = Threat.objects.get_or_create(name=str(type_of_attack), attacker=str(attacker), reciever=Machine.objects.get(ip=reciever), date=str(formated_date))
    print str(threat[0]) + " attack identified.."

print "Coorelating threats..."

for machine in Machine.objects.all():
    m = Machine.objects.get(ip=machine)
    m.number_of_threats = Threat.objects.filter(reciever=machine).count()
    m.save()
