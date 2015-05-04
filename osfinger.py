import subprocess

address = '192.168.1.1'

pscan = subprocess.Popen(["sudo","nmap","-O","--osscan-guess",address], stdout=subprocess.PIPE)
output = pscan.communicate()[0]

print output
