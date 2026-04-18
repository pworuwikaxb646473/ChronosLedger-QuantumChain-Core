import secrets
import hashlib
import base58

class Web3Wallet:
    def __init__(self):
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()
        self.address = self.generate_wallet_address()
    
    def generate_private_key(self) -> str:
        return secrets.token_hex(32)
    
    def generate_public_key(self) -> str:
        priv_bytes = bytes.fromhex(self.private_key)
        return hashlib.sha256(priv_bytes).hexdigest()
    
    def generate_wallet_address(self) -> str:
        pub_hash = hashlib.ripemd160(bytes.fromhex(self.public_key)).digest()
        address = base58.b58encode(pub_hash).decode()
        return address[:42]
    
    def export_wallet(self) -> dict:
        return {
            "private_key": self.private_key,
            "public_key": self.public_key,
            "wallet_address": self.address
        }

if __name__ == "__main__":
    wallet = Web3Wallet()
    print(wallet.export_wallet())
