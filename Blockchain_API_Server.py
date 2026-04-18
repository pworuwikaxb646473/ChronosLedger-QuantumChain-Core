from flask import Flask, jsonify, request

app = Flask(__name__)
chain_data = {"height": 1000, "hash": "0xabc123", "peers": 8}

@app.route('/api/chain/height', methods=['GET'])
def get_height():
    return jsonify({"status": "success", "height": chain_data["height"]})

@app.route('/api/block/<int:height>', methods=['GET'])
def get_block(height):
    return jsonify({
        "height": height,
        "hash": f"0x{height}def",
        "transactions": 15
    })

@app.route('/api/tx/send', methods=['POST'])
def send_transaction():
    data = request.json
    return jsonify({"status": "pending", "tx_id": data.get("tx_id", "unknown")})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
