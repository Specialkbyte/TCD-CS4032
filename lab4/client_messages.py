JOIN_MESSAGE = """
JOIN_CHATROOM: {chatroom}
CLIENT_IP: 0
PORT: 0
CLIENT_NAME: {handle}
"""

LEAVE_MESSAGE = """
LEAVE_CHATROOM: {room_ref}
JOIN_ID: {client_id}
CLIENT_NAME: {handle}
"""

SEND_MESSAGE = """
CHAT: {room_ref}
JOIN_ID: {client_id}
CLIENT_NAME: {handle}
MESSAGE: {message} \n\n
"""

DISCONNECT_MESSAGE = """
DISCONNECT: 0
PORT: 0
CLIENT_NAME: {handle}
"""