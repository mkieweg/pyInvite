from scapy.layers.inet import *
from scapy import route #even though pyCharm marks this as obsolete - it isn't


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
        for i in range(0,4):
            octets.append(random.randint(1,254))
        address = str(octets[0]) + '.' + str(octets[1]) + '.' + str(octets[2]) + '.' + str(octets[3])
        return address
