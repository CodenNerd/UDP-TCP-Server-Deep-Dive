from email import message
import socket

from constants import CHAR_ENCODING, MAX_SIZE_BYTES, SERVER_SOCKET_HOST, SERVER_SOCKET_PORT

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

message = input('Input lowercase sentence:')
data  = message.encode(CHAR_ENCODING)
s.sendto(data, ( SERVER_SOCKET_HOST, SERVER_SOCKET_PORT ))

print( 'OS assigned the address {} to client socket'.format(s.getsockname()) )

data, address = s.recvfrom(MAX_SIZE_BYTES)
text = data.decode(CHAR_ENCODING)

print('The server {} replied with {!r}'.format(address, text))
