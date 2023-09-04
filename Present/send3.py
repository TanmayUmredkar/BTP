# Sender.py
from pypresent import Present
import sys
import socket
import random
import string

# Generate a random text of a specified length
def generate_random_text(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Specify the length of the random text
random_text_length = 16  # You can change this to the desired length

# Generate a random text
text = generate_random_text(random_text_length)

k = "00000000000000000000"

if len(sys.argv) > 1:
    k = str(sys.argv[1])

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