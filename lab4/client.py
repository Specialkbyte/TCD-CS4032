

class Client:

  def __init__(handle):
    self.server_host = 'localhost'
    self.server_port = 8080
    self.handle = handle
    self.messages = []

    self._start()

  def _start():
    pass

  def join_chatroom(chatroom):
    pass

  def leave_chatroom(room_ref):
    pass

  def send_message(room_ref, message):
    pass

  def terminate_connection(handle):
    pass