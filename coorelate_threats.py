import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vent.settings')

import django
django.setup()

from topology.models import Machine, Threat

for machine in Machine.objects.all():
    m = Machine.objects.get(ip=machine)
    m.number_of_threats = Threat.objects.filter(reciever=machine).count()
    m.save()
