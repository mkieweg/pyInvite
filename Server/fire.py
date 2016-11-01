import socket


class Fire:
    @staticmethod
    def fire(address, payload):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.send(bytes(payload, 'utf-8'), (address, 50000))
