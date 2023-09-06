from pypresent import Present
import Padding
import sys
import socket

text = "text1234txet4321"
k = "00000000000000000000"

# if len(sys.argv) > 1:
#     text = str(sys.argv[1])

# if len(sys.argv) > 2:
#     k = str(sys.argv[2])

print('Text:\t' + text)
print('Key:\t' + k)
print('--------')
print()

key = bytes.fromhex(k)

# Create a socket connection
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_ip = '10.0.42.218'
receiver_port = 8000
receiver_address = (receiver_ip, receiver_port)
sender_socket.connect(receiver_address)

# Encrypt and send the text in 8-byte blocks
cipher = Present(key)
text_blocks = [text[i:i+7] for i in range(0, len(text), 7)]

for block in text_blocks:
    # Pad each block to 8 bytes if needed
    print(block)
    block = Padding.appendPadding(block, blocksize=8, mode='CMS')
    encrypted_block = cipher.encrypt(block.encode())
    print("Sending block:", encrypted_block)
    sender_socket.sendall(encrypted_block)

# Close the socket
sender_socket.close()
