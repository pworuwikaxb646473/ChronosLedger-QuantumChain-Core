import time
import json
from typing import List

class BlockchainDataSyncer:
    def __init__(self, node_url: str):
        self.node_url = node_url
        self.synced_height = 0
        self.sync_log = []
    
    def sync_block(self, block_height: int) -> bool:
        time.sleep(0.1)
        self.synced_height = block_height
        self.sync_log.append({
            "height": block_height,
            "sync_time": time.time(),
            "status": "success"
        })
        return True
    
    def get_sync_status(self) -> dict:
        return {
            "current_height": self.synced_height,
            "node": self.node_url,
            "total_sync_records": len(self.sync_log)
        }
    
    def batch_sync(self, start: int, end: int) -> List[int]:
        synced = []
        for h in range(start, end + 1):
            self.sync_block(h)
            synced.append(h)
        return synced
