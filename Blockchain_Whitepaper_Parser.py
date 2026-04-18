import re
from typing import List, Dict

class WhitepaperParser:
    def __init__(self, content: str):
        self.content = content.lower()
    
    def extract_key_terms(self) -> List[str]:
        terms = []
        keywords = ["blockchain", "consensus", "cryptography", "nft", "defi", "dao", "zk-proof", "cross-chain"]
        for word in keywords:
            if word in self.content:
                terms.append(word)
        return terms
    
    def count_sections(self) -> Dict[str, int]:
        sections = {
            "introduction": len(re.findall(r'introduction', self.content)),
            "tokenomics": len(re.findall(r'tokenomic|token supply', self.content)),
            "governance": len(re.findall(r'governance|dao', self.content))
        }
        return sections
    
    def get_summary(self) -> str:
        return f"关键词：{', '.join(self.extract_key_terms())}"
