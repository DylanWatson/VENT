from django.shortcuts import render
from django.http import HttpResponse
from topology.models import Machine, Threat,
from operator import itemgetter
import blackhole

def index(request):
    context_dict = {}
    machine_list = Machine.objects.all()
    context_dict['machines'] = machine_list
    context_dict['number_of_machines'] = len(machine_list)
    return render(request, 'topology/index.html', context_dict)

def machine(request, ip):
    context_dict = {}
    try:
        machine = Machine.objects.get(ip=ip)
        context_dict['machine_ip'] = machine

        threats = Threat.objects.filter(reciever=ip)
        context_dict['threats'] = threats

        #logic for obtaining the top 5 attacker
        attackers = []
        for threat in threats:
            attackers.append(str(threat.attacker))
        unique_attackers = list(set(attackers))
        attacker_and_attacks = []
        for unique_attacker in unique_attackers:
            count = 0
            for threat in threats:
                if unique_attacker == threat.attacker:
                    count = count + 1
            attacker_and_attacks.append((unique_attacker, count))
        attacker_and_attacks = sorted(attacker_and_attacks, key=lambda x: x[1], reverse=True)
        context_dict['top5'] = [x[0] for x in attacker_and_attacks[:5]]
        #Sort by number of threats
        #Save top 5 in context_dict so it can be accessed by machine.html
        #Maybe make cool visualizations? :)
        #Visualization of types of attacks :D

        #will need to check blackholed table to find out if machine is
        #blackholed or not in order to show proper options in drop-down




    except:
        pass


    return render(request, 'topology/machine.html', context_dict)


def attacker(request, ip):
    context_dict = {}

    threats = Threat.objects.filter(attacker=ip)
    context_dict['attacker'] = ip
    context_dict['threats'] = threats
    return render(request, "topology/attacker.html", context_dict)


    #will need to check blackholed table to find out if attacker is
    #blackholed or not in order to show proper options in drop-down


def blackhole_add(request, ip):
    context_dict = {}
    threats = Threat.objects.filter(attacker=ip)
    context_dict['attacker'] = ip
    context_dict['threats'] = threats

    bh = Blackhole.objects.get(ip=ip).blackholed
    if bh:
        context_dict['blackholed'] = 2  #normally 1 or 0 for T or F, 2 says to tell the user it was already T
    else
        blackhole.add()
        context_dict['blackholed'] = 1  #tell user blackhole was successful

    return render(request, "topology/blackhole_result.html", context_dict)

def blackhole_del(request, ip):
    context_dict = {}
    threats = Threat.objects.filter(attacker=ip)
    context_dict['attacker'] = ip
    context_dict['threats'] = threats

    bh = Blackhole.objects.get(ip=ip).blackholed
    if bh:
        blackhole.delete()
        context_dict['blackholed'] = 0  #tell user blackhole removal was successful
    else
        context_dict['blackholed'] = 3  #normally 1 or 0 for T or F, 3 says to tell the user it was already F

    return render(request, "topology/blackhole_result.html", context_dict)

def port_scan(request, ip):
    context_dict = {}
    #will add another parameter to determine the type of port scanning
    #do port scan stuff
    return render(request, "topology/portscan_results.html", context_dict)
