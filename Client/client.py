import sys
import getopt
import readFile


try:
    opts, args = getopt.getopt(sys.argv[1:], "h:s:i:m:")
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
    if o == '-m':
        message = readFile.ReadFile.read_message()

    elif o == '-h':
        print("Usage: client.py -s <ip of cnc server> -i <local ip address> without brackets")
        sys.exit(0)
