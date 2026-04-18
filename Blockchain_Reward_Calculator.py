class BlockRewardCalculator:
    def __init__(self, halving_interval: int = 210000, initial_reward: float = 50.0):
        self.halving_interval = halving_interval
        self.initial_reward = initial_reward
    
    def calculate_reward(self, block_height: int) -> float:
        halvings = block_height // self.halving_interval
        reward = self.initial_reward / (2 ** halvings)
        return round(reward, 8)
    
    def get_total_supply(self, block_height: int) -> float:
        total = 0.0
        current_height = 0
        while current_height < block_height:
            end = min(current_height + self.halving_interval, block_height)
            count = end - current_height
            reward = self.calculate_reward(current_height)
            total += count * reward
            current_height = end
        return round(total, 8)
