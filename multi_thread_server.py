import socket
import threading

def handle_client(c, addr):
    print(f"Connection from {addr}")
    with c:
        while True:
            data = c.recv(1024)
            # 當client端退出時，recv會返回空字串，這時就可以退出循環
            if not data:
                break
            c.sendall(data)
            print(f"addr: {addr}, data: {data.decode()}")
    print(f"Connection from {addr} closed")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1234))
    s.listen()
    print("Server is listening on port 1234...")

    while True:
        c, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(c, addr))
        t.start()