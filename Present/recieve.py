# Receiver.py
from pypresent import Present
import Padding
import sys
import socket

# Create a socket connection
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = 'RECEIVER_IP_ADDRESS'
receiver_port = 8000
receiver_address = (receiver_ip, receiver_port)
receiver_socket.bind(receiver_address)
receiver_socket.listen(1)
print("Waiting for connection...")
connection, sender_address = receiver_socket.accept()
print("Connected to", sender_address)

# Receive encrypted message
encrypted = connection.recv(1024)

# Close the connection
connection.close()

k = "00000000000000000000"
key = bytes.fromhex(k)

cipher = Present(key)

decrypted = cipher.decrypt(encrypted)

decrypted_text = Padding.removePadding(decrypted.decode(), blocksize=8, mode='CMS')
print('Decrypted:\t' + decrypted_text)
