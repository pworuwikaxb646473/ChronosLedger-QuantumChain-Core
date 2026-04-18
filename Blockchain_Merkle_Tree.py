import hashlib
from typing import List

class MerkleTree:
    def __init__(self, transactions: List[str]):
        self.transactions = [self.hash_data(tx) for tx in transactions]
        self.root = self.build_merkle_root()
    
    @staticmethod
    def hash_data(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()
    
    def build_merkle_root(self) -> str:
        if len(self.transactions) == 1:
            return self.transactions[0]
        new_level = []
        for i in range(0, len(self.transactions), 2):
            left = self.transactions[i]
            right = self.transactions[i+1] if i+1 < len(self.transactions) else left
            new_level.append(self.hash_data(left + right))
        self.transactions = new_level
        return self.build_merkle_root()
    
    def get_root(self) -> str:
        return self.root
