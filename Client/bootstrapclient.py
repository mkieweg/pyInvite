import socket

import Client.sendInvite
import Client.registerClient


class BootstrapClient:
    @staticmethod
    def bootstrap(serveraddress):
        r = Client.registerClient.RegisterClient(serveraddress, 40000)
        r.register()
        s = Client.sendInvite.SendInvite
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 50000))
        buffersize = 1024
        while 1:
            data = sock.recvfrom(buffersize)
            if data:
                s.fire(data)
