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

        if machine.number_of_threats < 5:
            context_dict["threat_level"] = "Low"

        if machine.number_of_threats < 10 and machine.number_of_threats >= 5:
            context_dict["threat_level"] = "Medium"

        if machine.number_of_threats < 15 and machine.number_of_threats >= 10:
            context_dict["threat_level"] = "High"

        if machine.number_of_threats >= 15:
            context_dict["threat_level"] = "Very High"

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
    attack_and_count = sorted(attack_and_count, key=lambda x: x[1], reverse=True)


    total = 0
    labels = []
    percentages = []
    for attack in attack_and_count:
        total = total + attack[1]

    for attack in attack_and_count:
        percentage =  float("{0:.2f}".format(float((attack[1]))/float(total)*100.0))
        make_attack(attack[0], percentage)

    context_dict["attacks"] = attack_object


    machines = Machine.objects.all()
    low_level = []
    medium_level = []
    high_level = []
    very_high_level = []
    for machine in machines:
        if machine.number_of_threats < 5:
            low_level.append(machine)

        if machine.number_of_threats < 10 and machine.number_of_threats >= 5:
            medium_level.append(machine)

        if machine.number_of_threats < 15 and machine.number_of_threats >= 10:
            high_level.append(machine)

        if machine.number_of_threats >= 15:
            very_high_level.append(machine)

    context_dict["low_level"] = low_level
    context_dict["medium_level"] = medium_level
    context_dict["high_level"] = high_level
    context_dict["very_high_level"] = very_high_level

    #Code here for displaying the IP addresses that were blacklisted
    #blacklisted = Blackhole.objects.all()
    #context_dict["blacklisted"] = blacklisted

    return render(request, "topology/report.html", context_dict)


def about(request):
    return render(request, "topology/about.html")
