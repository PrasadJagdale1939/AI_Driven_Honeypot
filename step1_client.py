import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1",9001))
    s.sendall(b"Hello Honypot")
    data = s.recv(1024)
    print(f"Server Replied : {data.decode1()}")