import time
import psutil
import socket

class NodeHealthChecker:
    def __init__(self, node_port: int):
        self.node_port = node_port
        self.check_history = []
    
    def check_port_open(self) -> bool:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex(('127.0.0.1', self.node_port))
        sock.close()
        return result == 0
    
    def check_system_load(self) -> dict:
        return {
            "cpu": psutil.cpu_percent(interval=0.5),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent
        }
    
    def full_health_check(self) -> dict:
        status = {
            "timestamp": time.time(),
            "port_open": self.check_port_open(),
            "system": self.check_system_load()
        }
        self.check_history.append(status)
        return status
