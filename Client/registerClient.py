import socket


class RegisterClient:
    serveraddress = "127.0.0.1"
    serverport = 40000
    local_ip = "120.0.0.1"
    s = None

    def __init__(self, serveraddress = None, serverport = None, local_ip = None):
        if serveraddress is not None and serverport is not None:
            self.serveraddress = serveraddress
            self.serverport = serverport
            self.local_ip = local_ip
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def register(self):
        self.s.sendto(bytes(self.local_ip, 'utf-8'), (self.serveraddress, self.serverport))
