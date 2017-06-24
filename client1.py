import socket

sock = socket.socket()
sock.connect(('localhost', 8080))
message = 'hello, world! My port is 8080'
sock.send(message.encode())

sock.close()
