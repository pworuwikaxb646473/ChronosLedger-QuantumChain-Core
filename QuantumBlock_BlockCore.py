import json
import time
from typing import List, Dict

class QuantumBlock:
    def __init__(self, index: int, previous_hash: str, transactions: List[Dict], timestamp: float = None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculate_block_hash()
    
    def calculate_block_hash(self) -> str:
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return __import__('hashlib').sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty: int):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_block_hash()
