import socket


class SendCustomPacket:
    s = None

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_custom_request(self, message, serveraddress):
        self.s.bind(("0.0.0.0", 5060))
        self.s.sendto(message, (serveraddress, 5060))
        data, addr = self.s.recvfrom(1024)
        print data
