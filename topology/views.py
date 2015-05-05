from django.shortcuts import render
from django.http import HttpResponse
from topology.models import Machine, Threat
from operator import itemgetter

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




    except:
        pass


    return render(request, 'topology/machine.html', context_dict)


def attacker(request, ip):
    context_dict = {}

    threats = Threat.objects.filter(attacker=ip)
    context_dict['attacker'] = ip
    context_dict['threats'] = threats
    return render(request, "topology/attacker.html", context_dict)

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
            if unique_attack == threat.attacker:
                count = count + 1
        attack_and_count.append((unique_attack, count))

    return render(request, "topology/report.html")
