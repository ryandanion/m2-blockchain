from Populate import *
from flask import Flask, jsonify, request
from SmartBlockchain import SmartBlockchain

app = Flask(__name__)
blockchain = SmartBlockchain()


@app.route("/mine", methods=["GET"])
def mine():
    last_block = blockchain.last_block()
    blockchain.new_block()
    response = {
        "message": "New block created",
        "index": last_block["index"],
        "transactions": last_block["transactions"],
        "previous_hash": last_block["previous_hash"],
    }
    return jsonify(response), 201


@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    body = request.get_json(force=True)
    required = ["sender", "amount", "receiver"]
    return body


if __name__ == "__main__":
    import sys

    populate = Populate()
    app.run(host="0.0.0.0", port=sys.argv[1])
