import sys
import getopt
import Client.bootstrapclient


try:
    opts, args = getopt.getopt(sys.argv[1:], "h:s:")
except getopt.GetoptError as e:
    print("Usage: client.py -s <serveraddress> without brackets\n")
    print("Use client.py -h for help")
    sys.exit(2)
if opts.__len__() is 0:
    print("Usage: client.py -s <serveraddress> without brackets")
    print("Use client.py -h for help")
    sys.exit(2)
for o, a in opts:
    if o == '-s':
        serveraddress = a
    elif o == '-h':
        print("Usage: client.py -s <serveraddress> without brackets")
        sys.exit(0)

bs = Client.bootstrapclient.BootstrapClient()
bs.bootstrap(serveraddress)
