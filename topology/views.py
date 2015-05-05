from django.shortcuts import render
from django.http import HttpResponse
from topology.models import Machine, Threat, Blackhole
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


        if machine.number_of_threats < 10 and machine.number_of_threats >= 5:
            context_dict["threat_level"] = "Medium"

        if machine.number_of_threats < 15 and machine.number_of_threats >= 10:
            context_dict["threat_level"] = "High"

        if machine.number_of_threats >= 15:
            context_dict["threat_level"] = "Very High"

    except:
        pass


    return render(request, 'topology/machine.html', context_dict)

def blackhole_add(request, ip):
    context_dict = {}
    threats = Threat.objects.filter(attacker=ip)
    context_dict['attacker'] = ip
    context_dict['threats'] = threats

    try:
        bh = Blackhole.objects.get(ip=ip).blackholed
        if bh == 1:
            context_dict['blackholed'] = 2  #normally 1 or 0 for T or F, 2 says to tell the user it was already T
        elif bh == 0:
            blackhole.add()
            context_dict['blackholed'] = 1  #tell user blackhole was successful
    except:
        blackhole.add()
        context_dict['blackholed'] = 1 #tell user blackhole was successful

    return render(request, "topology/blackhole_result.html", context_dict)

def blackhole_del(request, ip):
    context_dict = {}
    threats = Threat.objects.filter(attacker=ip)
    context_dict['attacker'] = ip
    context_dict['threats'] = threats

    try:
        bh = Blackhole.objects.get(ip=ip).blackholed
        if bh == 1:
            blackhole.delete()
            context_dict['blackholed'] = 0  #tell user blackhole removal was successful
        elif bh == 0:
            context_dict['blackholed'] = 3  #normally 1 or 0 for T or F, 3 says to tell the user it was already F
    except:
        blackhole.delete()
        context_dict['blackholed'] = 0

    return render(request, "topology/blackhole_result.html", context_dict)

def port_scan(request, ip):
    context_dict = {}
    #will add another parameter to determine the type of port scanning
    #do port scan stuff
    return render(request, "topology/portscan_results.html", context_dict)

def attackers(request):
    attacker_object = []

    class Attacker(object):
        ip=""
        number_of_attacks = 0

    def make_attacker(ip, number_of_attacks):
        attacker = Attacker()
        attacker.ip = ip
        attacker.number_of_attacks = number_of_attacks
        attacker_object.append(attacker)


    threats = Threat.objects.all()
    context_dict = {}
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
    for attacker in attacker_and_attacks:
        make_attacker(attacker[0], attacker[1])

    context_dict['sorted_attackers'] = attacker_object
    return render(request, "topology/attackers.html", context_dict)

def report(request):


    attack_object = []

    class Attack(object):
        attack_type=""
        percentage = float(0.0)

    def make_attack(attack_type, percentage):
        attack = Attack()
        attack.attack_type = attack_type
        attack.percentage = percentage
        attack_object.append(attack)

    threats = Threat.objects.all()
    context_dict = {}
    #logic for obtaining the top 5 attacker
    attacks = []
    for threat in threats:
        attacks.append(str(threat.name))
    unique_attacks = list(set(attacks))
    attack_and_count = []
    for unique_attack in unique_attacks:
        count = 0
        for threat in threats:
            if unique_attack == threat.name:
                count = count + 1
        attack_and_count.append((unique_attack, count))


    total = 0
    labels = []
    percentages = []
    for attack in attack_and_count:
        total = total + attack[1]

    for attack in attack_and_count:
        percentage =  float("{0:.2f}".format(float((attack[1]))/float(total)*100.0))
        make_attack(attack[0], percentage)

    context_dict["attacks"] = attack_object

    return render(request, "topology/report.html", context_dict)


def about(request):
    return render(request, "topology/about.html")
