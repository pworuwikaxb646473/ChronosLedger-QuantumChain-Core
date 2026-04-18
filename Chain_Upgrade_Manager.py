import time
from typing import Dict

class ChainUpgradeManager:
    def __init__(self, current_version: str):
        self.current_version = current_version
        self.upgrades = {}
        self.upgrade_id = 1
    
    def schedule_upgrade(self, height: int, new_version: str, details: str) -> int:
        upgrade = {
            "id": self.upgrade_id,
            "activate_height": height,
            "old_version": self.current_version,
            "new_version": new_version,
            "details": details,
            "status": "scheduled"
        }
        self.upgrades[self.upgrade_id] = upgrade
        self.upgrade_id += 1
        return upgrade["id"]
    
    def activate_upgrade(self, upgrade_id: int, current_height: int) -> bool:
        if upgrade_id not in self.upgrades:
            return False
        upg = self.upgrades[upgrade_id]
        if current_height >= upg["activate_height"]:
            upg["status"] = "activated"
            self.current_version = upg["new_version"]
            return True
        return False
    
    def get_version(self) -> str:
        return self.current_version
