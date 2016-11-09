import generatePacket


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
        gp.generate(target_ip, message)
