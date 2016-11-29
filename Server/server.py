import Queue
import threading, sys, getopt, socket
import fire
import time

f = fire.Fire()
serverdata = Queue.Queue()
sipserver = ""


def register_thread():
    """Provide UDP port awaiting client IP addresses and processing them into serverdata"""
    global serverdata
    print("Register Thread")
    print(serverdata.qsize())
    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("0.0.0.0", 40000))
        buffersize = 1024
        while 1:
            data = s.recvfrom(buffersize)
            decoded = data[0].decode()
            serverdata.put(decoded)
            # TODO: Cleanup debugging prints
            print("Client registerd")
            print(serverdata)
            print(serverdata.qsize())
        s.close()
        output = open('addresses', 'w')
        for item in serverdata:
            output.write("%s" % item)


def fire_thread():
    """Read client IP addresses and invokes fire() passing client IP address and server IP address"""
    used_addresses = []
    print("Fire Thread")
    print(serverdata.qsize())
    while 1:
        if not serverdata.empty():
            address = serverdata.get()
            if address not in used_addresses:
                f.fire(address, sipserver)
            used_addresses.append(address)


try:
    opts, args = getopt.getopt(sys.argv[1:], "h:s:")
except getopt.GetoptError as e:
    print("Usage: server.py -s <ip of sip server> without brackets")
    print("Use server.py -h for help")
    sys.exit(2)
if opts.__len__() is 0:
    print("Usage: server.py -s <ip of sip server> without brackets")
    print("Use server.py -h for help")
    sys.exit(2)
for o, a in opts:
    if o == '-s':
        sipserver = a
    elif o == '-h':
        print("Usage: server.py -s <serveraddress> without brackets")
        sys.exit(0)
register_thread_init = threading.Thread(target=register_thread)
register_thread_init.daemon = True
fire_thread_init = threading.Thread(target=fire_thread)
fire_thread_init.daemon = True
fire_thread_init.start()
register_thread_init.start()

while True:
    time.sleep(1)


