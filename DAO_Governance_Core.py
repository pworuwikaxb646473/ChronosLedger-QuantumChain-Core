from typing import Dict, List

class DAOGovernance:
    def __init__(self, proposal_fee: int = 10):
        self.proposals: Dict[int, dict] = {}
        self.proposal_id = 1
        self.proposal_fee = proposal_fee
        self.voters: Dict[str, int] = {}
    
    def create_proposal(self, creator: str, title: str, content: str) -> int:
        prop = {
            "id": self.proposal_id,
            "creator": creator,
            "title": title,
            "content": content,
            "votes_for": 0,
            "votes_against": 0,
            "status": "active"
        }
        self.proposals[self.proposal_id] = prop
        self.proposal_id += 1
        return prop["id"]
    
    def vote(self, voter: str, prop_id: int, support: bool, power: int):
        if prop_id not in self.proposals:
            return False
        prop = self.proposals[prop_id]
        if support:
            prop["votes_for"] += power
        else:
            prop["votes_against"] += power
        return True
