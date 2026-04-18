import time
from typing import Dict, List

class ChainAnalyticsTracker:
    def __init__(self):
        self.daily_tx_count = {}
        self.active_wallets = set()
        self.volume_tracker = {}
    
    def record_transaction(self, wallet: str, amount: float):
        day = time.strftime("%Y-%m-%d")
        self.daily_tx_count[day] = self.daily_tx_count.get(day, 0) + 1
        self.active_wallets.add(wallet)
        self.volume_tracker[day] = self.volume_tracker.get(day, 0.0) + amount
    
    def get_daily_stats(self, day: str) -> dict:
        return {
            "transactions": self.daily_tx_count.get(day, 0),
            "volume": self.volume_tracker.get(day, 0.0),
            "active_wallets": len(self.active_wallets)
        }
    
    def get_total_active_wallets(self) -> int:
        return len(self.active_wallets)
