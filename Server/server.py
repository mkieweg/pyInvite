import Server.data
import Server.register
import threading, sys, getopt
import Server.fire

r = Server.register.Register()
f = Server.fire.Fire()


def register_thread():
    while 1:
        r.register()


def fire_thread(sipserver):
    while 1:
        if Server.data.adresses.__len__() > 0:
            for address in Server.data.adresses:
                f.fire(address, sipserver)
                print("Fired against " % address)

try:
    opts, args = getopt.getopt(sys.argv[1:], "h:s:")
except getopt.GetoptError as e:
    print("Usage: client.py -s <sipserver> without brackets\n")
    print("Use client.py -h for help")
    sys.exit(2)
for o, a in opts:
    if o == '-s':
        sipserver = a
    elif o == '-h':
        print("Usage: client.py -s <serveraddress> without brackets")
        sys.exit(0)
register_thread_init = threading.Thread(target=register_thread())
fire_thread_init = threading.Thread(target=fire_thread())
register_thread_init.start()
fire_thread_init.start()
