import logging, socket

def client_send_message(port, message):
  BUFFER_SIZE = 1024

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  logging.info("Making connection to localhost:%d" % port)
  s.connect(('localhost', port))

  s.sendall(message)

  all_data = []
  while True:
    data = s.recv(BUFFER_SIZE)
    if not data:
      break
    else:
      all_data.append(data)
  s.close()

  return ''.join(all_data)