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
