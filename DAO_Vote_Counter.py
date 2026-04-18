from typing import Dict

class DAOVoteCounter:
    def __init__(self, quorum: float = 0.2):
        self.quorum = quorum
        self.proposal_results = {}
    
    def count_votes(self, proposal_id: int, votes_for: int, votes_against: int, total_supply: int) -> dict:
        total_votes = votes_for + votes_against
        quorum_met = (total_votes / total_supply) >= self.quorum
        passed = False
        if quorum_met:
            passed = votes_for > votes_against
        result = {
            "proposal_id": proposal_id,
            "quorum_met": quorum_met,
            "passed": passed,
            "votes_for": votes_for,
            "votes_against": votes_against,
            "total_votes": total_votes
        }
        self.proposal_results[proposal_id] = result
        return result
    
    def get_result(self, proposal_id: int) -> Dict:
        return self.proposal_results.get(proposal_id, {})
