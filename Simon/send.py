# Sender.py
import simon
import binascii
import sys
import socket

# Encryption key and plaintext message
k = '0x1b1a1918131211100b0a090803020100'
mess = 'hello'

# Convert message to binary
def getBinary(word):
    return int(binascii.hexlify(word), 16)

# Convert plaintext message to binary
m = getBinary(mess)

# Convert key to integer
key = int(k, 16)

# Create a socket connection
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = 'RECEIVER_IP_ADDRESS'
receiver_port = 'RECEIVER_PORT_NUMBER'
receiver_address = (receiver_ip, receiver_port)
sender_socket.connect(receiver_address)

# Send key and encrypted message to receiver
sender_socket.sendall(bytes(str(key), 'utf-8'))
sender_socket.sendall(bytes(str(m), 'utf-8'))

# Close the socket
sender_socket.close()
