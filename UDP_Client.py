from Client import Client

bytes_tosend = str.encode("test")
server_port = ("127.0.0.1", 20001)
bufferSize = 1024 
 

udp_client = Client('UDP', bufferSize)
udp_client.send_message(bytes_tosend, server_port)
msgFromServer = udp_client.receive_message()

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)