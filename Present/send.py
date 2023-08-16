# Sender.py
from pypresent import Present
import Padding
import sys
import socket

text = "help"
k = "00000000000000000000"

if len(sys.argv) > 1:
    text = str(sys.argv[1])

if len(sys.argv) > 2:
    k = str(sys.argv[2])

print('Text:\t' + text)
print('Key:\t' + k)
print('--------')
print()

key = bytes.fromhex(k)
text = Padding.appendPadding(text, blocksize=8, mode='CMS')

cipher = Present(key)

encrypted = cipher.encrypt(text.encode())

# Create a socket connection
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = 'RECEIVER_IP_ADDRESS'
receiver_port = 'RECEIVER_PORT_NUMBER'
receiver_address = (receiver_ip, receiver_port)
sender_socket.connect(receiver_address)

# Send encrypted message to receiver
sender_socket.sendall(encrypted)

# Close the socket
sender_socket.close()
