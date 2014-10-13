#!/usr/bin/python

'''
Author: Kevin Baker (11312066 - bakerke@tcd.ie)
Usage: ./echo-client.py << host >> << port >> << message >>

* HTTP GETs echo-server.php with query param message
* Does not support IPv6
'''

import sys
import socket

def echo_client_http_get(host, port, message):
  BUFFER_SIZE = 1024

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, port)) # does an internal dns lookup to convert the hostname into an IPv4 address

  # double line CRLF at the end to indicate end of http request
  http_request = "GET /echo-server.php?message=" + message + " HTTP/1.1\r\nHost: example.com\r\n\r\n"

  s.sendall(http_request)

  # loop to get all response packets from the echo-server
  # uppercased message might not be in the first data packet
  while True:
    data = s.recv(BUFFER_SIZE)
    if not data:
      break
    else:
      print repr(data) # don't pretty print it
  s.close()

if __name__ == "__main__":
  if len(sys.argv) is not 4:
    raise Exception("Usage: ./echo-client.py << host >> << port >> << message >>")
  host = sys.argv[1]
  port = int(sys.argv[2])
  message = sys.argv[3]

  echo_client_http_get(host, port, message)
