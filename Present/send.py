# Sender.py
from pypresent import Present
import Padding
import sys
import socket

text = "helphel"
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
print(type(encrypted))

# Create a socket connection
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = '10.0.42.218'
receiver_port = 8000
receiver_address = (receiver_ip, receiver_port)
sender_socket.connect(receiver_address)

# Send encrypted message to receiver
sender_socket.sendall(encrypted)

# Close the socket
sender_socket.close()
