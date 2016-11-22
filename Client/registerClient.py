import socket


class RegisterClient:
    """Registers client by cnc server."""
    server_address = "127.0.0.1"
    server_port = 40000
    local_ip = "120.0.0.1"
    s = None

    def __init__(self, server_address=None, server_port=None, local_ip=None):
        """Initializes the fields of the class. Receives address and port og the cnc server and clients IP address"""
        if server_address is not None and server_port is not None:
            self.server_address = server_address
            self.server_port = server_port
            self.local_ip = local_ip
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def register(self):
        """Sends UDP datagram containing the clients IP address to the cnc server."""
        self.s.sendto(bytes(self.local_ip), (self.server_address, self.server_port))
