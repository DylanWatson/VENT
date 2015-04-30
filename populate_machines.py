import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vent.settings')

import django
from vent import settings
django.setup()

from topology.models import Machine, Threat
import subprocess

if len(sys.argv) == 1:
    ip = settings.IP

    wildcard_position = 0
    if settings.SUBNET == "255.255.255.0":
        parts = ip.split('.')
        parts[3]="*"
        ip = "".join(str(parts[0])+"."+str(parts[1])+"."+str(parts[2])+"."+str(parts[3]))
        print "Subnet:" + ip

    if settings.SUBNET == "255.255.0.0":
        parts = ip.split('.')
        parts[2]="*"
        parts[3]="*"
        ip = "".join(str(parts[0])+"."+str(parts[1])+"."+str(parts[2])+"."+str(parts[3]))
        print "Subnet:" + ip


    print "Scanning Network..."
    test = subprocess.Popen(["sudo","nmap","-sP", ip], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    #parse for unique ip's
    #populate output
    need_mac = False	#nmap doesn't always find MAC's
    lines = output.split('\n')
    for line in lines[2:-2]:
        current_line = line.split()
        if len(current_line) == 6:
            if current_line[0] == "Nmap" and current_line[1] != "done:":
                ip = current_line[5].replace('(','').replace(')','')
                m = Machine.objects.get_or_create(ip=ip)
                print str(m[0]) + " Discovered"

        else:
            if current_line[0] == "Nmap" and current_line[1] != "done:":
                ip = current_line[4]
                m = Machine.objects.get_or_create(ip=ip)
                print str(m[0]) + " Discovered"

if len(sys.argv) == 2:
    if sys.argv[1] == "test":
        addresses = ["192.168.1.64", "192.168.15.4"]
        for address in addresses:
            m = Machine.objects.get_or_create(ip=address)
            print str(m[0]) + " Discovered"



        #High Level Threat
        ip = "192.168.12.149"
        m = Machine.objects.get_or_create(ip=ip)
        print str(m[0]) + " Discovered"

        #Very High Level Threat
        ip = "192.168.37.200"
        m = Machine.objects.get_or_create(ip=ip)
        print str(m[0]) + " Discovered"
