import socket
import threading
import json
from typing import Set

class P2PLedgerNetwork:
    def __init__(self, host: str = "0.0.0.0", port: int = 5678):
        self.host = host
        self.port = port
        self.peers: Set[str] = set()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"P2P节点启动：{self.host}:{self.port}")
        while True:
            conn, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_peer, args=(conn, addr)).start()
    
    def handle_peer(self, conn, addr):
        self.peers.add(str(addr))
        data = conn.recv(4096).decode('utf-8')
        if data:
            print(f"接收节点数据：{data}")
        conn.close()
    
    def broadcast_message(self, message: dict):
        msg = json.dumps(message).encode('utf-8')
        for peer in list(self.peers):
            try:
                peer_ip, peer_port = peer.split(':')
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((peer_ip, int(peer_port)))
                sock.sendall(msg)
                sock.close()
            except:
                self.peers.remove(peer)

if __name__ == "__main__":
    node = P2PLedgerNetwork()
    threading.Thread(target=node.start_server, daemon=True).start()
    input("P2P网络运行中...")
