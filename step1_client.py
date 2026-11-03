import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1",9001))
    msg = input("Type a Message: ")
    s.sendall(msg.encode())
    data = s.recv(1024)
    print(f"Server Replied : {data.decode()}")
    input("Press Enter to Disconnect...")