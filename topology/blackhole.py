import pxssh

def add(ip):
    #get ip address, username, and password for router
    bh = 'ip route add blackhole ' + ip
    h = '192.168.2.1'
    u = 'worthless_hack'
    p = 'FjRPZ0LO!'

    s = pxssh.pxssh()
    s.login(h, u, p)
    s.sendline(bh)
    s.logout()

def delete(ip):
    #get ip address, username, and password for router
    bh = 'ip route del blackhole ' + ip
    h = '192.168.2.1'
    u = 'worthless_hack'
    p = 'FjRPZ0LO!'

    s = pxssh.pxssh()
    s.login(h, u, p)
    s.sendline(bh)
    s.logout()
