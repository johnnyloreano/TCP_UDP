from Server import Server

localIP = "127.0.0.1"
localPort = 555
bufferSize = 1024
 
tcp_server = Server('TCP', bufferSize, localIP, localPort)

tcp_server.init_server(message = "Hello world!")