import json
import uuid
from dataclasses import dataclass
from typing import Optional

@dataclass
class NFTMetadata:
    name: str
    description: str
    image_url: str
    external_url: Optional[str] = None
    attributes: list = None

class NFTMetadataCreator:
    def __init__(self):
        self.token_id = str(uuid.uuid4())
    
    def create_metadata(self, name: str, desc: str, img_url: str, **kwargs) -> dict:
        metadata = NFTMetadata(
            name=name,
            description=desc,
            image_url=img_url,
            external_url=kwargs.get("external_url"),
            attributes=kwargs.get("attributes", [])
        )
        return {
            "token_id": self.token_id,
            "metadata": metadata.__dict__
        }
    
    def save_metadata_file(self, data: dict, file_path: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    creator = NFTMetadataCreator()
    meta = creator.create_metadata(
        name="QuantumNFT#001",
        desc="Chronos Ledger Genesis NFT",
        img_url="ipfs://QmXYZ123456789",
        attributes=[{"trait": "rarity", "value": "legendary"}]
    )
    print(json.dumps(meta, indent=2))
