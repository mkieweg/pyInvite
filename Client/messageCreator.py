import random
import string
from string import ascii_letters, digits


class MessageCreator:
    domains = ["REPLACED_DURING_RUNTIME", "evilshit.com", "localhost.com", "foo.bar.com", "h-da.de",
               "registrar.sip", "someschool.edu.com", "pyInvite.net", "siplink.co.nz"]

    methods = ["INVITE", "ACK", "BYE", "CANCEL", "REGISTER", "OPTIONS", "PRACK",
               "SUBSCRIBE", "NOTIFY", "PUBLISH", "INFO", "REFER", "MESSAGE", "UPDATE"]
    # "SIP/2.0",
    sequences = ["/UDP", "/TCP", "plain/text", "application/sdp"]
    mime_type = ["plain/text", "application/sdp"]
    names = ["alice", "anonymous", "bob", "ralph", "bernd", "sam", "daisy", "harold",
             "charlie", "michael", "alex", "rick", "jack", "john doe", "tom", "james", "birgit"]
    limits = {"maxforward": (190, 10),  # max , min
              "cseqlimit": (1999, 1),
              "contentlen": (980, 20),
              "taglimit": (3000, 2000)
              }

    def __init__(self):
        0 == 0

    def makeUA(self):
        ua = "sip:" + random.choice(self.names) + "@" + random.choice(self.domains)
        return ua

    def makeTag(self):
        tag = ";tag=" + str(random.randrange(1000, 10000)) + "@"
        socket = str(random.randrange(100, 170)) + "."
        socket += str(random.randrange(10, 109)) + "."
        socket += str(random.randrange(10, 109)) + "."
        socket += str(random.randrange(100, 120))
        tag += socket
        self.domains[0] = tag
        return tag

    def makeVia(self):
        via = "SIP/2.0" + random.choice(self.sequences) + " "
        via += str(random.randrange(100, 170)) + "."
        via += str(random.randrange(10, 109)) + "."
        via += str(random.randrange(10, 109)) + "."
        via += str(random.randrange(100, 120)) + ":5060"  # <- sip port
        # following branch maybe not needed
        via += ";branch=z9hG4bK"
        r = random.randint(4, 11)
        while r != 0:
            r -= 1
            via += random.choice(string.ascii_lowercase + digits)
        return via

    def makeCallID(self, host):
        callID = ""
        r = random.randint(8, 21)
        while r != 0:
            r -= 1
            callID += random.choice(string.ascii_lowercase + digits)
        callID += "@" + host
        return callID

    def make_message(self):
        target = self.makeUA()
        m = random.choice(self.methods) + " " + target + " " + "SIP/2.0" + "\n"  # 0
        m += "Via: " + self.makeVia() + "\n"  # 1
        m += "Max-Forwards: " + str(random.randrange(10, 201)) + "\n"  # 2
        m += "To: " + self.makeUA() + self.makeTag() + "\n"  # 3
        m += "From: " + target + "\n"  # 4
        m += "Call-ID: " + self.makeCallID(self.domains[0]) + "\n"  # 5
        m += "CSeq: " + str(random.randrange(1, 2000)) + " " + random.choice(self.methods) + "\n"  # 7
        tmp = str(random.randrange(20, 981))
        m += "Content-Type: " + random.choice(self.mime_type) + "\n"
        m += "Content-Length: " + tmp + "\n"  # 9
        return m
