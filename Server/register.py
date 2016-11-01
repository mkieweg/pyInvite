import socket
import Server.data


class Register:
    @staticmethod
    def register():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("0.0.0.0", 40000))
        buffersize = 1024
        while 1:
            data = s.recvfrom(buffersize)
            decoded = data[0].decode("utf-8")
            Server.data.adresses.append(decoded)
            # TODO: Cleanup debugging prints
            print("Client registerd")
            print(Server.data.adresses)
            print(Server.data.adresses.__len__())
        s.close()
        output = open('addresses', 'w')
        for item in Server.data.adresses:
            output.write("%s" % item)
