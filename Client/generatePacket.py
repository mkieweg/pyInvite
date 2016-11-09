from scapy.layers.inet import *


class GeneratePacket:
    def __init__(self):
        """Constructor"""

    def generate(self, target_ip, message):
        """Call the random_ip and send UDP packet with payload to that ip"""
        source_ip = self.random_ip()
        source_port = 10000 # source port
        destination_port = 5060 # destination port
        spoofed_packet = IP(src=source_ip, dst=target_ip) / UDP(sport=source_port, dport=destination_port) / message
        send(spoofed_packet)

    def random_ip(self):
        """Generate a random IP address"""
        octets = []
        for i in range(0,3):
            octets[i] = random.randint(1,254)
        address = octets[0] + '.' + octets[1] + '.' + octets[2] + '.' + octets[3]
        return address