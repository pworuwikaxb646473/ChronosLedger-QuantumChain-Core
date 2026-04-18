import random
import hashlib

class ZKProofSimulator:
    def __init__(self, secret: int):
        self.secret = secret
        self.modulus = 10007
    
    def commit(self) -> int:
        self.r = random.randint(1, 1000)
        return (self.secret * self.r) % self.modulus
    
    def generate_challenge(self) -> int:
        self.challenge = random.randint(1, 100)
        return self.challenge
    
    def prove(self) -> int:
        return (self.r * self.challenge) % self.modulus
    
    def verify(self, commit: int, proof: int) -> bool:
        left = (self.secret * proof) % self.modulus
        right = (commit * self.challenge) % self.modulus
        return left == right
