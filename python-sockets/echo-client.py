import socket
HOST = "127.0.0.1"  # the server's hostname or IP
PORT = 65432  # port used by server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"the, best")
    data = s.recv(1024)  # max no. of bytes to be received at once

print(f"Received {data}")
