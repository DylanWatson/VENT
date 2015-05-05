import subprocess
import commands


def force_scan(ip):
    address = ip
    f = open('scan.txt', 'w')
    pscan = subprocess.Popen(["sudo","nmap","-Pn","localhost"], stdout=subprocess.PIPE)
    output = pscan.communicate()[0]
    print (output)
    f.write(output)
    f.close()

def syn_scan(ip):
    address = ip
    f = open('scan.txt', 'w')
    pscan = subprocess.Popen(["sudo","nmap","-Pn", "-sS",address], stdout=subprocess.PIPE)
    output = pscan.communicate()[0]
    f.write(output)
    f.close()
