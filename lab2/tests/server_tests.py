import logging, socket, unittest

from testclient import client_send_message
from server import run_server

TEST_PORT = 8080
STUDENT_NUMBER = 11312066
HELO_RESPONSE = "HELO %s\nIP:localhost\nPort:%d\nStudentID:%d"
LONG_STRING = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce posuere nunc nulla, ac hendrerit dui scelerisque at. Nam venenatis suscipit consequat. Aenean libero mauris, fringilla vitae pulvinar at, facilisis non turpis. Quisque luctus risus magna, sed aliquet quam suscipit eget. Aliquam volutpat ipsum nec dapibus lobortis. Morbi dignissim ipsum orci, nec convallis metus commodo gravida. Curabitur diam quam, faucibus eu ultrices in, posuere eget arcu. Aenean tellus leo, ullamcorper ut justo eu, vestibulum hendrerit nulla. Cras arcu magna, fermentum id nibh eu, pretium ultricies ligula. Mauris viverra lacus eget mollis accumsan. Praesent suscipit justo a purus accumsan vehicula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce posuere nunc nulla, ac hendrerit dui scelerisque at. Nam venenatis suscipit consequat. Aenean libero mauris, fringilla vitae pulvinar at, facilisis non turpis. Quisque luctus risus magna, sed aliquet quam suscipit eget. Aliquam volutpat ipsum nec dapibus lobortis. Morbi dignissim ipsum orci, nec convallis metus commodo gravida. Curabitur diam quam, faucibus eu ultrices in, posuere eget arcu. Aenean tellus leo, ullamcorper ut justo eu."

class TestEchoMethods(unittest.TestCase):

  def test_simple_hello(self):
    '''Tests simple echo response returns information'''
    message = "test"
    resp = client_send_message(TEST_PORT, "HELO %s\n" % message)
    expected = self.helper_get_response(message)
    self.assertEqual(expected, resp)

  def test_long_hello(self):
    '''
    Tests that the server responds correctly if we send more
    than 1024 bytes
    '''
    message = LONG_STRING
    resp = client_send_message(TEST_PORT, "HELO %s\n" % message)
    expected = self.helper_get_response(message)
    self.assertEqual(expected, resp)

  def test_no_method(self):
    '''
    Tests that if we send an unrecognised command that the server
    responses with `Unrecognised Command`
    '''
    resp = client_send_message(TEST_PORT, "MANDRILL")
    expected = "UNRECOGNISED_COMMAND"
    self.assertEqual(expected, resp)

  def test_kill_service(self):
    '''
    Tests that if we send the kill service command
    that subsequent connections are refused
    '''
    resp = client_send_message(TEST_PORT, "KILL_SERVICE\n")
    self.assertEqual(resp, "SHUTTING_DOWN") # this method should 

    try:
      resp = self.test_simple_hello()
      self.assertEqual(resp, None)
    except socket.error(111, 'Connection refused'):
      return True # we want to get connection refused with this request

  def helper_get_response(self, message):
    return (HELO_RESPONSE % (message, TEST_PORT, STUDENT_NUMBER))
