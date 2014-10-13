import logging, unittest
from time import sleep
from threading import Thread

from testclient import client_send_message
from server import run_server

TEST_PORT = 8080
STUDENT_NUMBER = 11312066
HELO_RESPONSE = "HELO %s\nIP:localhost\nPort:%d\nStudentID:%d"

logging.basicConfig(level=logging.INFO)

class TestEchoMethods(unittest.TestCase):
  # @classmethod
  # def setUpClass(cls):
  #   print "Setting up test server"
  #   cls.server = Thread(target=run_server, args=(TEST_PORT,))
  #   cls.server.daemon = True
  #   cls.server.start()
  #   sleep(1)

  # @classmethod
  # def tearDownClass(cls):
  #   print "Tearing down test server"

  def test_simple_hello(self):
    message = "test"
    resp = client_send_message(TEST_PORT, "HELO %s\n" % message)
    expected = self.get_helo_response(message)
    self.assertEqual(expected, resp)

  def get_helo_response(self, message):
    return (HELO_RESPONSE % (message, TEST_PORT, STUDENT_NUMBER))
