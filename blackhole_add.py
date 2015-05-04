import getpass
import pxssh
import sys

#get ip address, username, and password for router
router_address = '192.168.2.1'#raw_input('Router IP: ')
malicious_address = sys.argv[1]#raw_input('Address to blackhole: ')
router_username = 'worthless_hack'#raw_input('Username: ')
router_password = sys.argv[2]#('Enter the router password to create blackhole: ')
print('Creating blackhole...')


try:
    ssh = pxssh.pxssh()
    ssh.login(router_address, router_username, router_password)
    ssh.sendline('ip route add blackhole ' + malicious_address)
    ssh.prompt()
    ssh.sendline('exit')
except Exception as e:
    print(str(e))

print(malicious_address + ' is now a blackhole')
