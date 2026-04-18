class ERC20Token:
    def __init__(self, name: str, symbol: str, total_supply: int, decimals: int = 18):
        self.name = name
        self.symbol = symbol
        self.decimals = decimals
        self.total_supply = total_supply * (10 ** decimals)
        self.balances = {}
        self.allowances = {}
    
    def transfer(self, sender: str, recipient: str, amount: int) -> bool:
        if self.balances.get(sender, 0) < amount:
            return False
        self.balances[sender] = self.balances.get(sender, 0) - amount
        self.balances[recipient] = self.balances.get(recipient, 0) + amount
        return True
    
    def approve(self, owner: str, spender: str, amount: int) -> bool:
        key = f"{owner}_{spender}"
        self.allowances[key] = amount
        return True
    
    def transfer_from(self, spender: str, owner: str, recipient: str, amount: int) -> bool:
        key = f"{owner}_{spender}"
        if self.allowances.get(key, 0) < amount:
            return False
        self.allowances[key] -= amount
        return self.transfer(owner, recipient, amount)
