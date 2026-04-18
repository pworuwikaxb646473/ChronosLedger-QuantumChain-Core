class GasEstimator:
    def __init__(self, base_fee: float = 10.0):
        self.base_fee = base_fee
        self.fee_multiplier = {"transfer": 1.0, "contract": 2.5, "nft_mint": 3.2}
    
    def estimate_gas(self, tx_type: str, data_size: int = 1) -> float:
        multiplier = self.fee_multiplier.get(tx_type, 1.5)
        base_cost = self.base_fee * multiplier
        size_penalty = data_size * 0.1
        return round(base_cost + size_penalty, 4)
    
    def dynamic_fee(self, network_congestion: float) -> float:
        if network_congestion > 0.8:
            return self.base_fee * 1.8
        elif network_congestion > 0.5:
            return self.base_fee * 1.3
        return self.base_fee
