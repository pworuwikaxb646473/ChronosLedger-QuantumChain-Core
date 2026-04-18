import hashlib
import ecdsa
import binascii

class TransactionSigner:
    def __init__(self, private_key_hex: str):
        self.private_key = ecdsa.SigningKey.from_string(
            binascii.unhexlify(private_key_hex),
            curve=ecdsa.SECP256k1
        )
    
    def sign_transaction(self, tx_data: dict) -> str:
        raw = str(tx_data).encode('utf-8')
        signature = self.private_key.sign_digest(
            hashlib.sha256(raw).digest()
        )
        return binascii.hexlify(signature).decode()
    
    @staticmethod
    def verify_signature(public_key_hex: str, tx_data: dict, signature: str) -> bool:
        vk = ecdsa.VerifyingKey.from_string(
            binascii.unhexlify(public_key_hex),
            curve=ecdsa.SECP256k1
        )
        raw = str(tx_data).encode('utf-8')
        try:
            return vk.verify(
                binascii.unhexlify(signature),
                hashlib.sha256(raw).digest()
            )
        except:
            return False
