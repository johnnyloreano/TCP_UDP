from Server import Server

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

udp_server = Server('UDP', bufferSize, localIP, localPort)

udp_server.init_server(message="Hello world!")
