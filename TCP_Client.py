from Client import Client

bytes_tosend = str.encode("test")
server_port = ("127.0.0.1", 555)
bufferSize = 1024

tcp_client = Client('TCP', bufferSize)
tcp_client.connect(server_port)

file = open("test.txt", "rb")
with open("test.txt", "rb") as f:
    byte = f.read(bufferSize)
    msg = tcp_client.send_message(byte, None)
    print(msg)
    while byte != b"":
        byte = f.read(bufferSize)
        msg = tcp_client.send_message(byte, None)
        print(msg)
