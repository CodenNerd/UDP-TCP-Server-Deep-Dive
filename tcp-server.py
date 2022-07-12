import socket
from constants import SERVER_SOCKET_PORT

from utils import recvall


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', SERVER_SOCKET_PORT))
sock.listen(1)
print('Listening at', sock.getsockname())
while True:
    print('Waiting for a new connection')
    sc, sockname = sock.accept()
    print('Connection from', sockname)
    print('  Socket name:', sc.getsockname())
    print('  Socket peer:', sc.getpeername())
    message = recvall(sc, 16)
    print('  message from client:', repr(message))
    sc.sendall(b'Goodbye, client!')
    sc.close()
    print('  Closing socket')