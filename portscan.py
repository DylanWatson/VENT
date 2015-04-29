import subprocess

address = '192.168.1.101'

pscan = subprocess.Popen(["sudo","nmap","-Pn",address], stdout=subprocess.PIPE)
output = pscan.communicate()[0]

print output
