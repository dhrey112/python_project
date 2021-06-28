import socket

target = "127.0.0.1"


def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False


for port in range(1, 501):
    if portscan(port):
        print("Port {} is open!".format(port))
    else:
        print(f"Port {port} is closed!")
