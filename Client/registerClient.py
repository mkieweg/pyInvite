import socket


class RegisterClient:
    """Registers client by cnc server."""
    serveraddress = "127.0.0.1"
    serverport = 40000
    local_ip = "120.0.0.1"
    s = None

    def __init__(self, serveraddress=None, serverport=None, local_ip=None):
        """Initializes the fields of the class. Receives address and port og the cnc server and clients IP address"""
        if serveraddress is not None and serverport is not None:
            self.serveraddress = serveraddress
            self.serverport = serverport
            self.local_ip = local_ip
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def register(self):
        """Sends UDP datagram containing the clients IP address to the cnc server."""
        self.s.sendto(bytes(self.local_ip, 'utf-8'), (self.serveraddress, self.serverport))
