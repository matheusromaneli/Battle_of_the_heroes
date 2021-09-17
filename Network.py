import socket

class Network():

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.71"
        self.port = 5555
        self.addr = (self.server,self.port)
        self.id = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, move):
        try:
            self.client.send(str.encode(move))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)