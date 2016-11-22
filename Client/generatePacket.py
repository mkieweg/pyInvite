from impacket import ImpactPacket
import randomIP


class GeneratePacket:
    @staticmethod
    def generate(message, target_ip):
        r = randomIP.RandomIP()
        src = r.random_ip()

        ip = ImpactPacket.IP()
        ip.set_ip_src(src)
        ip.set_ip_dst(target_ip)

        udp = ImpactPacket.UDP()
        udp.set_uh_sport(10000)
        udp.set_uh_dport(5060)
        udp.contains(ImpactPacket.Data(message))

        ip.contains(udp)
        return ip.get_packet()
