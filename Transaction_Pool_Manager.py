import time
from typing import List, Dict

class TransactionPool:
    def __init__(self, max_pool_size: int = 1000):
        self.pool: List[Dict] = []
        self.max_size = max_pool_size
    
    def add_transaction(self, tx: dict) -> bool:
        if len(self.pool) >= self.max_size:
            return False
        tx["add_time"] = time.time()
        tx["tx_id"] = self._generate_tx_id(tx)
        self.pool.append(tx)
        return True
    
    def _generate_tx_id(self, tx: dict) -> str:
        raw = f"{tx['from']}{tx['to']}{tx['amount']}{time.time()}"
        return __import__('hashlib').md5(raw.encode()).hexdigest()
    
    def get_pending_transactions(self, limit: int = 10) -> List[Dict]:
        return self.pool[:limit]
    
    def clear_transactions(self, tx_ids: List[str]):
        self.pool = [tx for tx in self.pool if tx["tx_id"] not in tx_ids]
