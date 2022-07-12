import socket
from constants import SERVER_SOCKET_PORT

from utils import recvall


host = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, SERVER_SOCKET_PORT))
print('Client has been assigned the socket: ', sock.getsockname())
sock.sendall(b'Greetings, server')
reply = recvall(sock, 16)
print('Server: ', repr(reply))
sock.close()
