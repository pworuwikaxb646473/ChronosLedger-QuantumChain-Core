import time
from typing import Dict, Optional

class NFTMarketplace:
    def __init__(self, platform_fee: float = 0.025):
        self.fee = platform_fee
        self.listings: Dict[str, dict] = {}
    
    def list_nft(self, nft_id: str, seller: str, price: float) -> bool:
        if nft_id in self.listings:
            return False
        self.listings[nft_id] = {
            "seller": seller,
            "price": price,
            "listed_at": time.time(),
            "sold": False
        }
        return True
    
    def buy_nft(self, nft_id: str, buyer: str) -> Optional[dict]:
        if nft_id not in self.listings:
            return None
        listing = self.listings[nft_id]
        if listing["sold"]:
            return None
        listing["sold"] = True
        platform_fee = listing["price"] * self.fee
        seller_receive = listing["price"] - platform_fee
        return {
            "nft_id": nft_id,
            "buyer": buyer,
            "seller": listing["seller"],
            "seller_receive": seller_receive,
            "platform_fee": platform_fee
        }
