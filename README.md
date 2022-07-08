# UDP-TCP-Client-Server-Deep-Dive


NOTES:

```
Host name#
The hostname is the IP address that your server will listen on. You can set it to one of three options:

- If you’re following along on your local machine, set it to 127.0.0.1 which is the localhost address, for IPV4. This address is called the loopback or localhost address and you should use this because you’ll be writing the client code on the same machine as the server. We’re doing the same here.

- You could also set it to the empty string '' which represents the INADDR_ANY. This specifies that the program intends to receive packets sent to the specified port destined for any of the IP addresses configured on that machine.

- Lastly, you could set it to a specific IP address assigned to your machine.

```
