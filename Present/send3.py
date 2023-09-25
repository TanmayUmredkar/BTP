# Sender.py
from pypresent import Present
import sys
import socket
import random
import string

# Generate a random text of a specified length
def generate_random_text(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Get the text as a command-line argument or generate random text
if len(sys.argv) > 1:
    text = str(sys.argv[1])
else:
    # Specify the length of the random text
    random_text_length = random.randint(1, 256)  # You can adjust the range as needed
    text = generate_random_text(random_text_length)

k = "00000000000000000000"

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

# Automatically adjust the chunk size based on message length
chunk_size = 1024  # Initial chunk size
while chunk_size < message_length:
    sender_socket.sendall(encrypted[:chunk_size])
    encrypted = encrypted[chunk_size:]
    chunk_size = min(chunk_size * 2, message_length)  # Double the chunk size, but not beyond the message length

# Close the socket
sender_socket.close()
