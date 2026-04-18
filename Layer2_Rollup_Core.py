import json
import hashlib
from typing import List

class Layer2Rollup:
    def __init__(self, chain_id: int):
        self.chain_id = chain_id
        self.batch_list = []
        self.batch_id = 1
    
    def create_batch(self, transactions: List[dict]) -> dict:
        batch = {
            "batch_id": self.batch_id,
            "chain_id": self.chain_id,
            "tx_count": len(transactions),
            "merkle_root": self._get_merkle_root(transactions),
            "status": "pending"
        }
        self.batch_list.append(batch)
        self.batch_id += 1
        return batch
    
    def _get_merkle_root(self, txs: List[dict]) -> str:
        if not txs:
            return "0"*64
        raw = json.dumps(txs, sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()
    
    def commit_batch(self, batch_id: int) -> bool:
        for b in self.batch_list:
            if b["batch_id"] == batch_id:
                b["status"] = "committed"
                return True
        return False
