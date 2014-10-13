#!/usr/bin/python

'''
Author: Kevin Baker (11312066 - bakerke@tcd.ie)
Usage: ./server.py << port >> << max_worker_threads >>
'''

import logging, socket, sys
import Queue
from time import sleep
from threading import Thread

MESSAGE = "IP:%s\nPort:%d\nStudentID:11312066"

def run_server(port, max_worker_threads=8, max_queue_size=100):
  host = 'localhost'
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  q = Queue.Queue(maxsize=max_queue_size)
  threads = []
  
  # connection handler
  def connection_handler(i, queue):
    BUFFER_SIZE = 1024

    while True:
      conn, addr = queue.get()

      logging.info("Thread recieved connection from queue from address %s:%d" % (addr[0], addr[1]))

      data = conn.recv(BUFFER_SIZE)

      if data == "KILL_SERVICE\n":
        logging.info("Server shutting down...")
        conn.close()
        raise NotImplemented("Finish this off")

      elif data[:4] == 'HELO':
        logging.info("Echoing message back returning student number")
        conn.sendall(data + (MESSAGE % (host, port)))

      else:
        logging.info("No handler for this type of request")

      conn.close()

  try:
    # setup thread pool
    for i in xrange(max_worker_threads):
      thread = Thread(target=connection_handler, args=(i, q))
      thread.daemon = True # daemonise so that KeyboardInterupt on main thread kills this thread too
      thread.start()
      
      threads.append(thread)

    # listen for connections and hand them off to a thread in the pool
    s.bind((host, port))
    s.listen(1)
    logging.info("Server has bound to socket on host '%s' and port '%d'" % (host, port))
    while True:
      conn, addr = s.accept()
      logging.info("Accepting connection from address '%s'" % addr[0])
      try:
        q.put((conn, addr), False) # do not block if queue is full - reject connection
      except Queue.Full:
        logging.info("Server overloaded cannot accept anymore connections")

    s.close()

  except (KeyboardInterrupt, SystemExit):
    print "Outter handler"
    sys.exit(0)

if __name__ == "__main__":
  if len(sys.argv) is not 3:
    raise Exception("Usage: ./server.py << port >> << max_worker_threads >>")
  port = int(sys.argv[1])
  max_worker_threads = int(sys.argv[2])

  logging.basicConfig(level=logging.INFO)

  run_server(port, max_worker_threads)