JOINED_CHATROOM_MESSAGE = """
JOINED_CHATROOM: %(chatroom)s
SERVER_IP: %(server_ip)s
PORT: %(server_port)d
ROOM_REF: %(room_ref)d
JOIN_ID: %(client_id)d
"""

LEFT_CHATROOM_MESSAGE = """
LEFT_CHATROOM: %(room_ref)d
JOIN_ID: %(client_id)d
"""

MESSAGE_MESSAGE = """
CHAT: %(room_ref)d
CLIENT_NAME: %(handle)s
MESSAGE: %(message)s \n\n
"""