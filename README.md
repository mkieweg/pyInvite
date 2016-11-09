pyInvite
==========
pyInvite is a tool that is used to test how your SIP server installation reacts to malformed SIP invite messages.
Written entirely for academic purposeses. Use it responsibly.

##Usage
pyInvite is written in python 3. Start programs with following parameters:
```
server.py -s <sip server>
  -s The sip servers IP address
client.py -s <cnc server> -i <local ip address>
  -s The command and control servers IP address
  -i The clients local IP address
```

##Startup
1. First start the server on the cnc machine. 
2. Then start the clients on the bots. 

###Take care of the right sequence
In this state it is nessecary that the server is startet before the clients. Clients register themselves by the server and there is no mechanism implemented to repeat registration after startup.

After startup the bot net works autonomous

##Dependencies
pyInvinte needs acapy-python3 for raw sockets
