import socket
import generatePacket
import messageCreator


class SendInvite:
    @staticmethod
    def fire(target_ip):
        """Send a SIP invite to the SIP server"""
        mc = messageCreator.MessageCreator()
        gp = generatePacket.GeneratePacket()
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        i = 0
        while i < 10:
            message = mc.make_message()
            s.sendto(gp.generate(message, target_ip), (target_ip, 0))
            i += 1
