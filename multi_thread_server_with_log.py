import socket
import threading
import logging

# 1. 設定 logging 格式與輸出目標
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("server_log.txt", mode="a", encoding="utf-8"), # 寫入檔案（Append 模式）
        logging.StreamHandler()                                            # 同時印在控制台 (Console)
    ]
)

def handle_client(c, addr):
    logging.info(f"Connection from {addr}")
    try:
        with c:
            while True:
                data = c.recv(1024)
                # 當 client 端退出時，recv 會返回空字串，這時就可以退出循環
                if not data:
                    break

                # 處理收到的資料（轉碼並去除末端換行/回車，避免 Log 多空行）
                decoded_data = data.decode(errors='replace').rstrip('\r\n')
                logging.info(f"addr: {addr}, data: {decoded_data}")

                c.sendall(data)
    finally:
        logging.info(f"Connection from {addr} closed")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1234))
    s.listen()
    logging.info("Server is listening on port 1234...")

    try:
        while True:
            c, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(c, addr))
            t.start()
    except KeyboardInterrupt:
        pass
    finally:
        logging.info("Server stopped")

    