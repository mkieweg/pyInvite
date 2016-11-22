import random


class RandomIP:
    """Generate a random IP address"""
    random_array = []


    def __init__(self):
        """Initialize the random array"""
        for i in range(1,255):
            self.random_array.append(i)

    def random_ip(self):
        """Generate a random IP address"""
        octets = []
        for i in range(0,4):
            octets.append(random.choice(self.random_array))
        address = str(octets[0]) + '.' + str(octets[1]) + '.' + str(octets[2]) + '.' + str(octets[3])
        return address