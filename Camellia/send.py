import socket

# Initialize Camellia and encryption mode (e.g., ECB)
from camellia import Camellia, ECB  # Assuming you have a Camellia module

# Define the encryption key
encryption_key = b'MySecretKey12345'  # Change this to your actual encryption key

# Create a Camellia instance with the key
camellia = Camellia(encryption_key)

# Create an ECB encryptor
ecb_encryptor = ECB(camellia)

# Create a socket to send the encrypted message
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = "192.168.178.221"
receiver_port = 8000
sender_socket.connect((receiver_ip, receiver_port))

# Encrypt the plaintext message
plaintext_message = "Your plaintext message here"
encrypted_message = camellia.encode(plaintext_message.encode())

# Send the encrypted message to Raspberry Pi 2
for block in encrypted_message:
    sender_socket.send(block)

sender_socket.close()
