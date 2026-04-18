from typing import List, Dict
import hashlib

class MultiSigWallet:
    def __init__(self, owners: List[str], required: int):
        self.owners = owners
        self.required = required
        self.transactions: Dict[str, dict] = {}
        self.approvals: Dict[str, List[str]] = {}
    
    def create_transaction(self, to: str, value: float) -> str:
        tx_id = hashlib.sha256(f"{to}{value}".encode()).hexdigest()
        self.transactions[tx_id] = {"to": to, "value": value, "executed": False}
        self.approvals[tx_id] = []
        return tx_id
    
    def approve_transaction(self, owner: str, tx_id: str) -> bool:
        if owner not in self.owners:
            return False
        if tx_id not in self.transactions:
            return False
        if owner in self.approvals[tx_id]:
            return False
        self.approvals[tx_id].append(owner)
        return True
    
    def execute_transaction(self, tx_id: str) -> bool:
        if len(self.approvals[tx_id]) >= self.required:
            self.transactions[tx_id]["executed"] = True
            return True
        return False
