import socket

class Client:

    def __init__(self, kind, buffer):
        self.buffer = buffer
        self.kind = socket.SOCK_DGRAM if kind == 'UDP' else socket.SOCK_STREAM

        self.client = socket.socket(family=socket.AF_INET, type=self.kind)
    
    def send_message(self,data,port):
        if self.kind == socket.SOCK_DGRAM:
            self.client.sendto(data, port)
            return self.client.recvfrom(self.buffer)
        else:
            self.client.sendall(data)
            res = self.client.recv(self.buffer)
            return res

    def connect(self,port):
        self.client.connect(port)