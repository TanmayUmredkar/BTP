# Receiver.py
from pypresent import Present
import sys
import socket

# Create a socket connection
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = 'RECEIVER_IP_ADDRESS'  # Replace with the actual receiver's IP
receiver_port = 8000
receiver_address = (receiver_ip, receiver_port)
receiver_socket.bind(receiver_address)
receiver_socket.listen(1)
print("Waiting for connection...")
connection, sender_address = receiver_socket.accept()
print("Connected to", sender_address)

# Receive the length of the message
message_length_bytes = connection.recv(4)
message_length = int.from_bytes(message_length_bytes, byteorder='big')

# Receive encrypted message
encrypted = connection.recv(message_length)

# Close the connection
connection.close()

k = "00000000000000000000"
key = bytes.fromhex(k)

cipher = Present(key)

decrypted = cipher.decrypt(encrypted)

decrypted_text = decrypted.decode()
print('Decrypted:\t' + decrypted_text)
