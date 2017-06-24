import socket
import util

print('server started')
recv_sock = socket.socket()
send_sock = socket.socket()

util.createSocket(recv_sock, '', 8080)
util.createSocket(send_sock, '', 9090)

# connection and address
recv_conn, recv_addr = util.connect(recv_sock)
if recv_conn and recv_addr:
    print('connected client:', recv_addr)
send_conn, send_addr = util.connect(send_sock)
if send_conn and send_addr:
    print('connected client:', send_addr)

while True:
    data = recv_conn.recv(1024)
    if not data:
        break
    send_conn.send(data)
