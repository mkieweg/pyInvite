import random
import socket


class SendInvite:
    @staticmethod
    def fire(target_ip, packet_array):
        """Send a SIP invite to the SIP server"""
        rng = random.Random()
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        i = 0
        while True:
            packet = packet_array[rng.randint(0, 99999)]
            s.sendto(packet, (target_ip, 0))
