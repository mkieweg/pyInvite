import random
import string
from string import ascii_letters, digits


#gernerating random sip messages

domains=[ "REPLACED_DURING_RUNTIME","evilshit.com" ,"localhost.com", "foo.bar.com", "h-da.de",
        "registrar.sip", "someschool.edu.com", "pyInvite.net", "siplink.co.nz"]

methods=["INVITE","ACK", "BYE", "CANCEL", "REGISTER", "OPTIONS", "PRACK",
    "SUBSCRIBE", "NOTIFY", "PUBLISH", "INFO", "REFER", "MESSAGE", "UPDATE"]
#"SIP/2.0",
sequences=["/UDP", "/TCP","plain/text", "application/sdp"]
type=["plain/text", "application/sdp"]
names=["alice", "anonymous", "bob", "ralph", "bernd", "sam", "daisy", "harold",
    "charlie", "michael", "alex", "rick", "jack", "john doe", "tom", "james", "birgit", "lassmiranda", "dennsiewillja"]
limits={"maxforward":(190,10),#max , min
        "cseqlimit":(1999,1),
        "contentlen":(980,20),
        "taglimit":(3000,2000)
        }
def makeUA():
    ua="sip:"+random.choice(names)+"@"+random.choice(domains)
    return ua

def makeTag():
    tag=";tag="+str(random.randrange(1000,10000))+"@"
    socket=str(random.randrange(100,170))+"."
    socket+=str(random.randrange(10,109))+"."
    socket+=str(random.randrange(10,109))+"."
    socket+=str(random.randrange(100,120))
    tag+=socket
    domains[0]=tag
    return tag

def makeVia():
    via="SIP/2.0"+random.choice(sequences)+" "
    via+=str(random.randrange(100,170))+"."
    via+=str(random.randrange(10,109))+"."
    via+=str(random.randrange(10,109))+"."
    via+=str(random.randrange(100,120))+":5060" #<- sip port
    #following branch maybe not needed
    via+=";branch=z9hG4bK"
    r=random.randint(4,11)
    while r!=0:
        r-=1
        via+=random.choice(string.ascii_lowercase+digits)
    return via

def makeCallID(host):
    callID=""
    r=random.randint(8,21)
    while r!=0:
        r-=1
        callID+=random.choice(string.ascii_lowercase+digits)
    callID+="@"+host
    return callID

def makeMessege():
    target=makeUA()
    m=random.choice(methods)+" "+target+" "+"SIP/2.0"+"\n"     #0
    m+="Via: "+makeVia()+"\n"    #1
    m+="Max-Forwards: "+str(random.randrange(10,201))+"\n"    #2
    m+="To: "+makeUA()+makeTag()+"\n"  #3
    m+="From: "+target+"\n" #4
    m+="Call-ID: "+makeCallID(domains[0])+"\n"  #5
    m+="CSeq: "+str(random.randrange(1,2000))+" "+random.choice(methods)+"\n"  #7
    tmp=str(random.randrange(20,981))
    m+="Content-Type: "+random.choice(type)+"\n"
    m+="Content-Length: "+tmp+"\n"#9
    print(m)
    return m

makeMessege()