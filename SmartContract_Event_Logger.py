import json
import time
from typing import Any

class ContractEventLogger:
    def __init__(self, contract_name: str):
        self.contract = contract_name
        self.events = []
    
    def emit_event(self, event_name: str, data: Any):
        event = {
            "contract": self.contract,
            "event": event_name,
            "timestamp": time.time(),
            "data": data,
            "event_id": self._generate_event_id()
        }
        self.events.append(event)
        return event
    
    def _generate_event_id(self) -> str:
        raw = f"{self.contract}_{time.time()}_{random.random()}"
        return hashlib.sha1(raw.encode()).hexdigest()
    
    def export_events(self) -> str:
        return json.dumps(self.events, indent=2)
