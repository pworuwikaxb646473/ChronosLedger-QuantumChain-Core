import json
import hashlib
from typing import Optional

class CrossChainBridge:
    def __init__(self, source_chain: str, target_chain: str):
        self.source = source_chain
        self.target = target_chain
        self.bridge_id = self._generate_bridge_id()
    
    def _generate_bridge_id(self) -> str:
        raw = f"{self.source}_{self.target}_{random.random()}"
        return hashlib.md5(raw.encode()).hexdigest()
    
    def lock_asset(self, user_addr: str, amount: float, token: str) -> dict:
        return {
            "bridge_id": self.bridge_id,
            "action": "lock",
            "user": user_addr,
            "amount": amount,
            "token": token,
            "source_chain": self.source
        }
    
    def mint_asset(self, lock_data: dict) -> Optional[dict]:
        if lock_data.get("bridge_id") == self.bridge_id:
            return {
                "bridge_id": self.bridge_id,
                "action": "mint",
                "user": lock_data["user"],
                "amount": lock_data["amount"],
                "token": lock_data["token"],
                "target_chain": self.target
            }
        return None
