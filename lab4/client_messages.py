JOIN_MESSAGE = """
JOIN_CHATROOM: %(chatroom)s
CLIENT_IP: 0
PORT: 0
CLIENT_NAME: %(handle)s
"""

LEAVE_MESSAGE = """
LEAVE_CHATROOM: %(room_ref)d
JOIN_ID: %(client_id)d
CLIENT_NAME: %(handle)s
"""

SNED_MESSAGE = """
CHAT: %(room_ref)d
JOIN_ID: %(client_id)d
CLIENT_NAME: %(handle)s
MESSAGE: %(message)s \n\n
"""

DISCONNECT_MESSAGE = """
DISCONNECT: 0
PORT: 0
CLIENT_NAME: %(handle)s
"""