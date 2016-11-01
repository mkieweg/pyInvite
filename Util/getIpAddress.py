import socket


class GetIpAddress:
    @staticmethod
    def get_ip_address():
        addr_obj = socket.gethostbyname_ex(socket.gethostname())
        return addr_obj[2][1]