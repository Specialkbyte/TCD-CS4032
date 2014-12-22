import logging, socket

from client_messages import JOIN_MESSAGE, LEAVE_MESSAGE, SEND_MESSAGE, DISCONNECT_MESSAGE

BUFFER_SIZE = 1024

class Client:

  def __init__(self, handle):
    self.server_port = 8081
    self.handle = handle
    self.messages = []
    self.client_id = 0

    logging.info("Client making connection to localhost:%d" % self.server_port)
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.connect(('localhost', self.server_port))

  def join_chatroom(self, chatroom):
    message = JOIN_MESSAGE.format(
      chatroom=chatroom,
      handle=self.handle
    )
    self._send_message(message)

  def leave_chatroom(self, room_ref):
    message = LEAVE_MESSAGE.format(
      room_ref=room_ref, 
      client_id=self.client_id, 
      handle=self.handle
    )
    self._send_message(message)

  def send_message(self, room_ref, message):
    message = SEND_MESSAGE.format(
      room_ref=room_ref,
      client_id=self.client_id,
      handle=self.handle,
      message=self.message
    )
    self._send_message(message)

  def terminate_connection(self, handle):
    message = DISCONNECT_MESSAGE.format(
      handle=self.handle
    )

  def _send_message(self, message):
    self.s.sendall(message)
    logging.info("Sending: " + message)

    data = self.s.recv(BUFFER_SIZE) # TODO fix this

    logging.info("Received response: " + data)