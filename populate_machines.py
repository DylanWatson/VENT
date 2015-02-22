import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vent.settings')

import django
django.setup()

from topology.models import Machine
import subprocess
import re

test = subprocess.Popen(["sudo","nmap","-sP","192.168.1.*"], stdout=subprocess.PIPE)
output = test.communicate()[0]
#parse for unique ip's
#populate output
need_mac = False	#nmap doesn't always find MAC's
lines = output.split('\n')
for line in lines[2:-1]:
    current_line = line.split()
    if current_line[0] == "Nmap" and current_line[1] != "done:":
        ip = current_line[4]
        m = Machine.objects.get_or_create(ip=ip)[0]
