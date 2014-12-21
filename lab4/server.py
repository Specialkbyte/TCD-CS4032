#!/usr/bin/python

'''
Author: Kevin Baker (11312066 - bakerke@tcd.ie)
Usage: ./server.py << port >> << max_worker_threads >>
'''

import logging, socket, sys
import Queue
from time import sleep
from threading import Thread
from multiprocessing import Value

def route_message(data):
  '''Figures out what kind of command the request is'''
  pass

def client_join_chatroom(data):
  pass

def client_leave_chatroom(data):
  pass

def client_disconnect(data):
  pass

def client_sent_message(data):
  pass

def run_server(port, max_worker_threads=8, max_queue_size=100):
  host = 'localhost'
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  q = Queue.Queue(maxsize=max_queue_size)
  threads = []

  # connection handler
  def connection_handler(queue):
    BUFFER_SIZE = 8096

    while True:
      conn, addr = queue.get()

      logging.info("Thread recieved connection from queue from address %s:%d" % (addr[0], addr[1]))

      data = conn.recv(BUFFER_SIZE) # doesn't handle messages longer than BUFFER_SIZE

      route_message(data)

  try:
    # setup thread pool
    for i in xrange(max_worker_threads):
      thread = Thread(target=connection_handler, args=(q))
      thread.daemon = True # daemonise so that KeyboardInterupt on main thread kills these threads too
      thread.start()
      
      threads.append(thread)

    # listen for connections and hand them off to a thread in the pool
    s.bind((host, port))
    s.listen(1)
    logging.info("Server has bound to socket on host '%s' and port '%d'" % (host, port))
    while True
      # accept connections
      conn, addr = s.accept()
      logging.info("Accepting connection from address '%s'" % addr[0])
      try:
        q.put((conn, addr), False) # do not block if queue is full - reject connection
      except Queue.Full:
        logging.info("Server overloaded cannot accept anymore connections")

    s.close()

  except (KeyboardInterrupt, SystemExit):
    logging.info("END: Shutting down service")
    sys.exit(0)

if __name__ == "__main__":
  if len(sys.argv) is not 3:
    raise Exception("Usage: ./server.py << port >> << max_worker_threads >>")
  port = int(sys.argv[1])
  max_worker_threads = int(sys.argv[2])

  # logging stuff
  FORMAT = "%(asctime)s %(process)s %(thread)s: %(message)s"
  logging.basicConfig(format=FORMAT, level=logging.INFO)

  run_server(port, max_worker_threads)
