import requests
import time
from typing import Optional

class BlockchainOracle:
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.last_update = 0
        self.cached_data = {}
    
    def fetch_price(self, symbol: str) -> Optional[float]:
        if time.time() - self.last_update < 10:
            return self.cached_data.get(symbol)
        try:
            res = requests.get(self.api_url, params={"symbol": symbol}, timeout=5)
            data = res.json()
            price = float(data["price"])
            self.cached_data[symbol] = price
            self.last_update = time.time()
            return price
        except:
            return self.cached_data.get(symbol)
    
    def get_last_update_time(self) -> float:
        return self.last_update
