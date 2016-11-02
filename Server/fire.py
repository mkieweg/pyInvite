import socket


class Fire:
    """Send target IP to the client"""
    s = None

    def __init__(self):
        """Initialize the class' field"""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def fire(self, address, payload):
        """Send target IP to the client"""
        self.s.sendto(bytes(payload, 'utf-8'), (address, 50000))
        return 0
