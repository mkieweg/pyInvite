import random
import string
from string import digits


class MessageCreator:
    domains = ["REPLACED_DURING_RUNTIME", "evilshit.com", "localhost.com", "foo.bar.com", "h-da.de",
               "registrar.sip", "someschool.edu.com", "pyInvite.net", "siplink.co.nz"]

    # "SIP/2.0",
    sequences = ["/UDP", "/TCP", "plain/text", "application/sdp"]
    mime_type = ["plain/text", "application/sdp"]
    sender_names = ["alice", "anonymous", "bob", "ralph", "bernd", "sam", "daisy", "harold",
             "charlie", "michael", "alex", "rick", "jack", "john doe", "tom", "james", "birgit"]
    receiver_names = []
    limits = {"maxforward": (190, 10),  # max , min
              "cseqlimit": (1999, 1),
              "contentlen": (980, 20),
              "taglimit": (3000, 2000)
              }

    def __init__(self, receiver_names):
        self.receiver_names = receiver_names

    def make_ua(self):
        ua = "sip:" + random.choice(self.receiver_names) + "@141.100.71.125"
        return ua

    def make_sender(self):
        ua = "sip:" + random.choice(self.sender_names) + "@" + random.choice(self.domains)
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

    def make_via(self):
        via = "SIP/2.0" + random.choice(self.sequences) + " "
        via +=  "141.100.71.125:5060"
        # following branch maybe not needed
        via += ";branch=z9hG4bK"
        r = random.randint(4, 11)
        while r != 0:
            r -= 1
            via += random.choice(string.ascii_lowercase + digits)
        return via

    def make_call_id(self, host):
        call_id = ""
        r = random.randint(8, 21)
        while r != 0:
            r -= 1
            call_id += random.choice(string.ascii_lowercase + digits)
        call_id += "@" + host
        return call_id

    def make_message(self):
        target = self.make_sender()
        m = "INVITE" + " " + target + " " + "SIP/2.0" + "\n"  # 0
        m += "Via: " + self.make_via() + "\n"  # 1
        m += "Max-Forwards: " + str(random.randrange(10, 201)) + "\n"  # 2
        m += "To: " + self.make_ua() + self.makeTag() + "\n"  # 3
        m += "From: " + target + "\n"  # 4
        m += "Call-ID: " + self.make_call_id("141.100.71.125") + "\n"  # 5
        m += "CSeq: " + str(random.randrange(1, 2000)) + " " + "INVITE\n\n"  # 7
        return m
