# Receiver.py
import simon
import binascii
import sys
import socket

# Create a socket connection
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = 'RECEIVER_IP_ADDRESS'
receiver_port = 'RECEIVER_PORT_NUMBER'
receiver_address = (receiver_ip, receiver_port)
receiver_socket.bind(receiver_address)
receiver_socket.listen(1)
print("Waiting for connection...")
connection, sender_address = receiver_socket.accept()
print("Connected to", sender_address)

# Receive key and encrypted message
key_str = connection.recv(1024).decode('utf-8')
m_str = connection.recv(1024).decode('utf-8')

# Convert key and message to integers
key = int(key_str, 16)
m = int(m_str, 10)

# Close the connection
connection.close()

# Decryption process
ksize = (len(key_str) - 2) * 4
bsize = 32
if ksize == 72:
    bsize = 48
elif ksize == 96:
    bsize = 48
elif ksize == 128:
    bsize = 64

w = simon.SimonCipher(key, key_size=ksize, block_size=bsize)

res = w.decrypt(m)
res_str = bytes.fromhex(hex(res)[2:]).decode('utf-8')
print("Decrypted:", res_str)
