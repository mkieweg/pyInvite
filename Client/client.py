import sys, getopt, socket

from Client import registerClient
from Client import sendInvite


try:
    opts, args = getopt.getopt(sys.argv[1:], "h:s:")
except getopt.GetoptError as e:
    print("Usage: client.py -s <serveraddress> without brackets\n")
    print("Use client.py -h for help")
    sys.exit(2)
for o, a in opts:
    if o == '-s':
        serveraddress = a
    elif o == '-h':
        print("Usage: client.py -s <serveraddress> without brackets")
        sys.exit(0)

r = registerClient.RegisterClient(serveraddress, 40000)
r.register()
s = sendInvite.SendInvite
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 50000))
buffersize = 1024
while 1:
    data = sock.recvfrom(buffersize)
    if data:
        s.fire(data)
