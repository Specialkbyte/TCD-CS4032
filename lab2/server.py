#!/usr/bin/python

'''
Author: Kevin Baker (11312066 - bakerke@tcd.ie)
Usage: ./server.py << port >> << max_worker_threads >>
'''

import signal, socket, sys
from time import sleep
from threading import Thread

def run_server(port, max_worker_threads):
  host = '' # all interfaces
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # setup handler if process killed
  def shutdown_server(*args):
    s.close()
    sys.exit(0)

  signal.signal(signal.SIGINT, shutdown_server)
  signal.signal(signal.SIGTERM, shutdown_server)

  # connection handler
  def connection_handler(conn, addr):
    print 'Connected by', addr

    conn.sendall("Testing\r\n")
    for i in xrange(10):
      conn.sendall(str(i) + "\r\n")
      sleep(1)
    conn.sendall("Done\r\n")
    conn.close()

  # listen for connections and hand them off to a thread in the pool
  s.bind((host, port))
  s.listen(1)
  while True:
    conn, addr = s.accept()
    thread = Thread(target=connection_handler, args=(conn, addr))
    thread.start()
  s.close()

if __name__ == "__main__":
  if len(sys.argv) is not 3:
    raise Exception("Usage: ./server.py << port >> << max_worker_threads >>")
  port = int(sys.argv[1])
  max_worker_threads = sys.argv[2]

  run_server(port, max_worker_threads)