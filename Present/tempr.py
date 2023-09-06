from pypresent import Present
import Padding
import socket

# Receiver configuration
receiver_ip = '10.0.42.218'  # Listen on all available network interfaces
receiver_port = 8000

# Create a socket for receiving connections
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_address = (receiver_ip, receiver_port)
receiver_socket.bind(receiver_address)
receiver_socket.listen(1)

print("Waiting for connection...")
connection, sender_address = receiver_socket.accept()
print("Connected to", sender_address)

# Receive and decrypt the encrypted message
encrypted_blocks = b''  # Initialize an empty bytes object to store received blocks


# Decryption key
k = "00000000000000000000"
key = bytes.fromhex(k)

# Decrypt and remove padding
cipher = Present(key)
decrypted_text = ''
while True:
    block = connection.recv(1024)  # Receive a block (maximum 1024 bytes)
    if not block:
        break  # Break the loop when no more data is received (connection closed)
    decrypted_block = cipher.decrypt(block)
    # print(decrypted_block)
    decrypted_text +=  Padding.removePadding(decrypted_block.decode(), blocksize=8, mode='CMS')

# Close the connection and socket
connection.close()
receiver_socket.close()

# # Decrypt each 8-byte block separately
# for i in range(0, len(encrypted_blocks), 7):
#     block = encrypted_blocks[i:i + 7]
#     # print(block)
#     decrypted_block = cipher.decrypt(block)
#     # print(decrypted_block)
#     decrypted_text += decrypted_block.decode()
#     # print(len(decrypted_text))

print('Decrypted:\t' + decrypted_text)
