from email import message
import socket

from constants import CHAR_ENCODING, MAX_SIZE_BYTES, SERVER_SOCKET_HOST, SERVER_SOCKET_PORT

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

hosts = []

while True:
    host = input('Input host address: ')
    port = int(input('Input host port: '))
    hosts.append((host, port))
    message = input('Input lowercase sentence:')
    data  = message.encode(CHAR_ENCODING)
    s.sendto(data, (host, port))

    print( 'OS assigned the address {} to client socket'.format(s.getsockname()) )

    data, address = s.recvfrom(MAX_SIZE_BYTES)
    text = data.decode(CHAR_ENCODING)
    if (address in hosts):
        print('The server {} replied with {!r}'.format(address, text))
    else:
        print('message {!r} from unexpected host {}!'.format(text, address))