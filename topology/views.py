from django.shortcuts import render
from django.http import HttpResponse
from topology.models import Machine, Threat, Blackhole
from operator import itemgetter
import blackhole
from datetime import datetime
import portscan

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


        #get blackhole status
        try:
            context_dict['blackholed'] = Blackhole.objects.get(ip=ip).blackholed
        except:
            context_dict['blackholed'] = 0

    except:
        pass


    return render(request, 'topology/machine.html', context_dict)

def attacker(request, ip):
    context_dict = {}

    threats = Threat.objects.filter(attacker=ip)
    context_dict['attacker'] = ip
    context_dict['threats'] = threats
    context_dict['count'] = threats.count()

    #get blackhole status
    try:
        context_dict['blackholed'] = Blackhole.objects.get(ip=ip).blackholed
    except:
        context_dict['blackholed'] = 0

    return render(request, "topology/attacker.html", context_dict)

def admin_actions(request, ip):
    context_dict = {}
    action = request.POST['action_list']
    if action == '0':
        return port_scan(request, ip)
    elif action == '1':
        return blackhole_add(request, ip)
    elif action == '2':
        return blackhole_del(request, ip)

def blackhole_add(request, ip):
    context_dict = {}
    threats = Threat.objects.filter(attacker=ip)
    context_dict['attacker'] = ip
    context_dict['threats'] = threats

    bh = 0
    try:
        bh = Blackhole.objects.get_or_create(ip=ip)
        if bh[0].blackholed == 1:
            context_dict['blackholed'] = 2  #normally 1 or 0 for T or F, 2 says to tell the user it was already T
        elif bh[0].blackholed == 0:
            blackhole.add(ip)
            bh[0].blackholed = 1
            bh[0].date = datetime.now()
            bh[0].save()
            context_dict['blackholed'] = 1  #tell user blackhole was successful
    except:
        #blackhole.add(ip)
        context_dict['blackholed'] = bh #tell user blackhole was successful

    all_holes = Blackhole.objects.all()
    context_dict['all_holes'] = all_holes
    return render(request, "topology/blackhole_result.html", context_dict)

def blackhole_del(request, ip):
    context_dict = {}
    threats = Threat.objects.filter(attacker=ip)
    context_dict['attacker'] = ip

    try:
        bh = Blackhole.objects.get_or_create(ip=ip)
        if bh[0].blackholed == 1:
            blackhole.delete(ip)
            bh[0].blackholed = 0
            bh[0].date = datetime.now()
            bh[0].save()
            context_dict['blackholed'] = 0  #tell user blackhole removal was successful
        elif bh[0].blackholed == 0:
            context_dict['blackholed'] = 3  #normally 1 or 0 for T or F, 3 says to tell the user it was already F
    except:
        context_dict['blackholed'] = 4

    all_holes = Blackhole.objects.all()
    context_dict['all_holes'] = all_holes
    return render(request, "topology/blackhole_result.html", context_dict)

def port_scan(request, ip):
    ports = []
    states = []
    services = []
    have_to_keep_count = []
    temp_count = 0
    context_dict = {}
    context_dict['ip'] = ip

    if '192.168.' in ip:
        portscan.force_scan(ip)
    else:
        portscan.syn_scan(ip)

    with open('scan.txt') as f:
        for line in f:
            parts = line.split()
            try:
                if '/' in parts[0]:
                    ports.append(parts[0])
                    states.append(parts[1])
                    services.append(parts[2])
                    temp_count += 1
                    have_to_keep_count.append(temp_count)
            except:
                pass

    context_dict['ports'] = ports
    context_dict['states'] = states
    context_dict['services'] = services
    context_dict['count'] = have_to_keep_count

    return render(request, "topology/portscan_results.html", context_dict)

def scan(request):
    scan_object = []

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
