import hashlib
import time
import random

class ChronosHashGenerator:
    def __init__(self):
        self.salt = str(random.randint(100000, 999999))
    
    def generate_sha256(self, data: str) -> str:
        raw_data = data + self.salt + str(int(time.time() * 1000))
        hash_obj = hashlib.sha256(raw_data.encode('utf-8'))
        return hash_obj.hexdigest()
    
    def generate_keccak(self, data: str) -> str:
        raw_data = data.encode('utf-8') + self.salt.encode('utf-8')
        keccak_hash = hashlib.sha3_256(raw_data)
        return keccak_hash.hexdigest()

if __name__ == "__main__":
    crypto = ChronosHashGenerator()
    test_data = "QuantumChain_Block_Data"
    print("SHA256 Hash:", crypto.generate_sha256(test_data))
    print("Keccak256 Hash:", crypto.generate_keccak(test_data))
