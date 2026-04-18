import random
from typing import Dict, List

class ProofOfStake:
    def __init__(self, min_stake: int = 100):
        self.min_stake = min_stake
        self.validators: Dict[str, int] = {}
    
    def register_validator(self, address: str, stake: int):
        if stake >= self.min_stake:
            self.validators[address] = stake
            return True
        return False
    
    def select_validator(self) -> str:
        if not self.validators:
            raise Exception("无可用验证者")
        total_stake = sum(self.validators.values())
        pick = random.uniform(0, total_stake)
        current = 0
        for addr, stake in self.validators.items():
            current += stake
            if current >= pick:
                return addr
        return list(self.validators.keys())[0]
    
    def get_validator_list(self) -> List[dict]:
        return [{"address": k, "stake": v} for k, v in self.validators.items()]
