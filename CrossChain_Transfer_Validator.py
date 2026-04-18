import hashlib
from typing import Optional

class CrossChainTransferValidator:
    def __init__(self, trusted_bridge: str):
        self.trusted_bridge = trusted_bridge
    
    def validate_transfer(self, transfer_data: dict) -> Optional[dict]:
        if transfer_data.get("bridge_address") != self.trusted_bridge:
            return None
        if transfer_data.get("amount", 0) <= 0:
            return None
        proof = self._generate_proof(transfer_data)
        return {
            "valid": True,
            "proof": proof,
            "chain_pair": f"{transfer_data['source']}_{transfer_data['target']}"
        }
    
    def _generate_proof(self, data: dict) -> str:
        raw = f"{data['tx_id']}{data['amount']}{self.trusted_bridge}"
        return hashlib.sha256(raw.encode()).hexdigest()
