import threading, sys, getopt, socket
import fire

f = fire.Fire()
serverdata = []
sipserver = ""


def register_thread():
    global serverdata
    print("Register Thread")
    print(serverdata.__len__())
    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("0.0.0.0", 40000))
        buffersize = 1024
        while 1:
            data = s.recvfrom(buffersize)
            decoded = data[0].decode("utf-8")
            serverdata.append(decoded)
            # TODO: Cleanup debugging prints
            print("Client registerd")
            print(serverdata)
            print(serverdata.__len__())
        s.close()
        output = open('addresses', 'w')
        for item in serverdata:
            output.write("%s" % item)


def fire_thread():
    print("Fire Thread")
    print(serverdata.__len__())
    while 1:
        if serverdata.__len__() > 0:
            for address in serverdata:
                f.fire(address, sipserver)
            print(serverdata)

try:
    opts, args = getopt.getopt(sys.argv[1:], "h:s:")
except getopt.GetoptError as e:
    print("Usage: client.py -s <ip of sip server> without brackets")
    print("Use client.py -h for help")
    sys.exit(2)
if opts.__len__() is 0:
    print("Usage: client.py -s <ip of sip server> without brackets")
    print("Use client.py -h for help")
    sys.exit(2)
for o, a in opts:
    if o == '-s':
        sipserver = a
    elif o == '-h':
        print("Usage: client.py -s <serveraddress> without brackets")
        sys.exit(0)
register_thread_init = threading.Thread(target=register_thread)
fire_thread_init = threading.Thread(target=fire_thread)
fire_thread_init.start()
register_thread_init.start()
