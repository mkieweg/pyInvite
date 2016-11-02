import socket


class Fire:
    s = None

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def fire(self, address, payload):
        self.s.sendto(bytes(payload, 'utf-8'), (address, 50000))
        return 0
