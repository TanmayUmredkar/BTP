import socket

# Initialize Camellia and encryption mode (e.g., ECB)
from camellia import Camellia, ECB  # Assuming you have a Camellia module

# Define the encryption key
encryption_key = b'MySecretKey12345'  # Use the same key as in Raspberry Pi 1

# Create a Camellia instance with the key
camellia = Camellia(encryption_key)

# Create an ECB decryptor
ecb_decryptor = ECB(camellia)

# Create a socket to receive the encrypted message
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = "192.168.178.221"
receiver_port = 8000
receiver_socket.bind((receiver_ip, receiver_port))
receiver_socket.listen(1)

print("Waiting for a connection...")
connection, sender_address = receiver_socket.accept()
print("Connected to sender:", sender_address)

# Receive the encrypted message
received_encrypted_message = b""
while True:
    data = connection.recv(1024)
    if not data:
        break
    received_encrypted_message += data

# Decrypt the received message
decrypted_message = camellia.decode(received_encrypted_message)

# Print the decrypted message
print("Decrypted Message:", decrypted_message.decode())

connection.close()
