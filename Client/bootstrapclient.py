import socket

import sendInvite
import registerClient


class BootstrapClient:
    @staticmethod
    def bootstrap(serveraddress, local_ip):
        r = registerClient.RegisterClient(serveraddress, 40000, local_ip)
        r.register()
        s = sendInvite.SendInvite
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 50000))
        buffersize = 1024
        while 1:
            data = sock.recvfrom(buffersize)
            if data:
                decoded = data[0].decode("utf-8")
                s.fire(decoded)
