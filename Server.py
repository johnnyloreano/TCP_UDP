import socket


class Server:

    def __init__(self, kind, buffer, ip, port):
        self.ip = ip
        self.port = port
        self.buffer = buffer
        self.kind = socket.SOCK_DGRAM if kind == 'UDP' else socket.SOCK_STREAM
        self.client = socket.socket(family=socket.AF_INET, type=self.kind)

    def init_server(self, message="Server is up!"):
        return self.init_udp() if self.kind == socket.SOCK_DGRAM else self.init_tcp()

    def init_udp(message="Server is up!"):
        self.client.bind((self.ip, self.port))
        print("Server is up!")
        while(True):

            client_message, address = self.client.recvfrom(self.buffer)

            print("Message from Client:{}".format(client_message))
            print("Client IP Address:{}".format(address))

            self.client.sendto(str.encode(message), address)

    def init_tcp(self):
        print("Initializing TCP Server...")
        with self.client as s:
            s.bind((self.ip, self.port))
            s.listen()
            conn, addr = s.accept()
            print("TCP Server up!")
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(self.buffer)
                    if not data:
                        break
                    else:
                        print(data)
                    conn.sendall(data)
