import socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram
CHAR_ENCODING = 'ascii'

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
port = 3000
hostname = '127.0.0.1'
s.bind(( hostname, port ))
print('Listening at {}' . format(s.getsockname()))

while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES) # Receive at most 65535 bytes at once
    message = data.decode(CHAR_ENCODING)
    upperCaseMessage = message.upper()
    print( 'The client at {} says {!r}'.format(clientAddress, message) )
    data = upperCaseMessage.encode(CHAR_ENCODING)
    s.sendto( data, clientAddress )