from email import message
import socket

from constants import CHAR_ENCODING, MAX_SIZE_BYTES, SERVER_SOCKET_HOST, SERVER_SOCKET_PORT

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
s.connect( ( SERVER_SOCKET_HOST, SERVER_SOCKET_PORT ) )
message = input('Input lowercase sentence:')
data  = message.encode(CHAR_ENCODING)
s.send(data)

print( 'OS assigned the address {} to client socket'.format(s.getsockname()) )

data = s.recv(MAX_SIZE_BYTES)
text = data.decode(CHAR_ENCODING)

print('The server replied with {!r}'.format(text))
