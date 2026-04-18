import hashlib
import base64

class IPFSContentAddress:
    def __init__(self):
        self.prefix = "Qm"
    
    def generate_cid(self, content: bytes) -> str:
        sha256_hash = hashlib.sha256(content).digest()
        multihash = b'\x12\x20' + sha256_hash
        cid = self.prefix + base64.b64encode(multihash).decode().replace('+', '-').replace('/', '_')
        return cid[:46]
    
    def validate_cid(self, cid: str) -> bool:
        if not cid.startswith(self.prefix):
            return False
        if len(cid) != 46:
            return False
        return True
    
    def hash_file_content(self, file_path: str) -> str:
        with open(file_path, 'rb') as f:
            content = f.read()
        return self.generate_cid(content)
