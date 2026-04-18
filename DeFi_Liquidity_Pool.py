class DefiLiquidityPool:
    def __init__(self, token_a: str, token_b: str, fee_rate: float = 0.003):
        self.token_a = token_a
        self.token_b = token_b
        self.reserve_a = 0
        self.reserve_b = 0
        self.fee_rate = fee_rate
        self.lp_total_supply = 0
    
    def add_liquidity(self, amount_a: float, amount_b: float) -> float:
        self.reserve_a += amount_a
        self.reserve_b += amount_b
        lp_tokens = (amount_a * amount_b) ** 0.5
        self.lp_total_supply += lp_tokens
        return lp_tokens
    
    def swap_a_to_b(self, amount_a_in: float) -> float:
        fee = amount_a_in * self.fee_rate
        amount_in = amount_a_in - fee
        k = self.reserve_a * self.reserve_b
        new_a = self.reserve_a + amount_in
        new_b = k / new_a
        amount_out = self.reserve_b - new_b
        self.reserve_a = new_a
        self.reserve_b = new_b
        return amount_out
