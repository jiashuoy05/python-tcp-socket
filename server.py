import socket

# AF_INET: IPv4, SOCK_STREAM: TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1234)) # 綁定IP地址和端口號
    s.listen() # 監聽連接
    print("Server is listening on port 1234...")
    c, addr = s.accept() # 接受客戶端的連接
    with c:
        print(f"Connected by {addr}") # 印出客戶端的地址
        while True:
            data = c.recv(1024) # 接收客戶端發送的數據，最大接收 1024 Bytes (1KB)
            if not data:
                break 
            c.sendall(data) # 回傳接收到的數據給客戶端