import socket
import Util.getIpAddress


class RegisterClient:
    serveraddress = "127.0.0.1"
    serverport = 40000
    s = None

    def __init__(self, serveraddress = None, serverport = None):
        if serveraddress is not None and serverport is not None:
            self.serveraddress = serveraddress
            self.serverport = serverport
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def register(self):
        gip = Util.getIpAddress.GetIpAddress()
        ownip = gip.get_ip_address()
        self.s.sendto(bytes(ownip, 'utf-8'), (self.serveraddress, self.serverport))
