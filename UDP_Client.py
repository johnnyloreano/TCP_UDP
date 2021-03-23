from Client import Client

bytes_tosend = str.encode("test")
server_port = ("127.0.0.1", 20001)
bufferSize = 1024

udp_client = Client('UDP', bufferSize)

with open("testBigFile.txt", "rb") as f:
    byte = f.read(bufferSize)
    msg = udp_client.send_message(byte, server_port)
    print(msg)
    while byte != b"":
        byte = f.read(bufferSize)
        msg = udp_client.send_message(byte, server_port)
        print(msg)
