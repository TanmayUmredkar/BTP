# Sender.py
from pypresent import Present
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

cipher = Present(key)

encrypted = cipher.encrypt(text.encode())

# Create a socket connection
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = 'RECEIVER_IP_ADDRESS'  # Replace with the actual receiver's IP
receiver_port = 8000
receiver_address = (receiver_ip, receiver_port)
sender_socket.connect(receiver_address)

# Send the length of the message
message_length = len(encrypted)
sender_socket.sendall(message_length.to_bytes(4, byteorder='big'))

# Send encrypted message to receiver
sender_socket.sendall(encrypted)

# Close the socket
sender_socket.close()
