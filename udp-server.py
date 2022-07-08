import socket

from constants import CHAR_ENCODING, MAX_SIZE_BYTES, SERVER_SOCKET_HOST, SERVER_SOCKET_PORT

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

s.bind(( SERVER_SOCKET_HOST, SERVER_SOCKET_PORT ))
print('Listening at {}' . format(s.getsockname()))

while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES) # Receive at most 65535 bytes at once
    message = data.decode(CHAR_ENCODING)
    upperCaseMessage = message.upper()
    print( 'The client at {} says {!r}'.format(clientAddress, message) )
    data = upperCaseMessage.encode(CHAR_ENCODING)
    s.sendto( data, clientAddress )