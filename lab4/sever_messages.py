JOINED_CHATROOM_MESSAGE = """
JOINED_CHATROOM: {chatroom}
SERVER_IP: {server_ip}
PORT: {server_port}
ROOM_REF: {room_ref}
JOIN_ID: {client_id}
"""

LEFT_CHATROOM_MESSAGE = """
LEFT_CHATROOM: {room_ref}
JOIN_ID: {client_id}
"""

MESSAGE_MESSAGE = """
CHAT: {room_ref}
CLIENT_NAME: {handle}
MESSAGE: {message} \n\n
"""

ERROR_MESSAGE = """
ERROR_CODE: {code}
ERROR_DESCRIPTION: {reason}
"""