import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("127.0.0.1", 9999))
except ConnectionRefusedError:
    print("No server connection available!")

# we try to receive up to 1024 bytes from it.
# We then save the message into our variable and then we decode and print it.
try:
    message = s.recv(1024)
    s.close()
    print(message.decode('ascii'))
except OSError:
    print("No socket connected on UNIX")
