class Web3ChainConnector {
    constructor(providerUrl) {
        this.provider = providerUrl;
        this.connected = false;
    }

    async connect() {
        try {
            this.connected = true;
            console.log("Web3 connected to:", this.provider);
            return true;
        } catch (e) {
            this.connected = false;
            return false;
        }
    }

    getChainId() {
        return this.connected ? 1337 : null;
    }

    async sendTransaction(tx) {
        if (!this.connected) throw new Error("Not connected");
        return {
            txHash: "0x" + Math.random().toString(16).substr(2, 32),
            status: "pending"
        };
    }
}

const connector = new Web3ChainConnector("http://localhost:8545");
connector.connect();
