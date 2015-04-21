import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vent.settings')

import django
from vent import settings
django.setup()

from topology.models import Machine, Threat
import subprocess

ip = settings.IP

wildcard_position = 0
if settings.SUBNET == "255.255.255.0":
    parts = ip.split('.')
    parts[3]="*"
    ip = "".join(str(parts[0])+"."+str(parts[1])+"."+str(parts[2])+"."+str(parts[3]))
    print ip

if settings.SUBNET == "255.255.0.0":
    parts = ip.split('.')
    parts[2]="*"
    parts[3]="*"
    ip = "".join(str(parts[0])+"."+str(parts[1])+"."+str(parts[2])+"."+str(parts[3]))
    print ip

test = subprocess.Popen(["sudo","nmap","-sP", ip], stdout=subprocess.PIPE)
output = test.communicate()[0]
#parse for unique ip's
#populate output
need_mac = False	#nmap doesn't always find MAC's
lines = output.split('\n')
for line in lines[2:-1]:
    current_line = line.split()
    if current_line[0] == "Nmap" and current_line[1] != "done:":
        ip = current_line[5].replace('(','').replace(')','')
        m = Machine.objects.get_or_create(ip=ip)[0]
        print str(m) + " Discovered"
