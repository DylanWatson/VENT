import getpass
import pxssh
import sys

#get ip address, username, and password for router
router_address = '192.168.2.1'#raw_input('Router IP: ')
malicious_address = sys.argv[1]#raw_input('Address to remove blackhole: ')
router_username = 'worthless_hack'#raw_input('Username: ')
router_password = sys.argv[2]#getpass.getpass('Enter the router password to remove blackhole: ')
print('Removing blackhole...')


try:
    ssh = pxssh.pxssh()
    ssh.login(router_address, router_username, router_password)
    ssh.sendline('ip route del blackhole ' + malicious_address)
    ssh.prompt()
    ssh.sendline('exit')
except Exception as e:
    print(str(e))

print('Blackhole removed from ' + malicious_address)
