import json
import time
import hashlib


class SmartBlockchain:
    def __init__(self, current_transactions=[], chain=[]):
        self.current_transactions = current_transactions
        self.chain = chain
        self.genesis_block()

    def hash(self, value):
        return hashlib.sha256(value)

    def hash_to_json(self):
        return json.loads(self.last_block().decode("utf-8"))

    def dict_to_hash(self, value):
        return hashlib.sha256(
            json.dumps(value, sort_keys=True).encode("utf-8")
        ).hexdigest()

    def genesis_block(self):
        block = {
            "index": 0,
            "timestamp": time.time(),
            "transactions": self.current_transactions,
            "previous_hash": 0,
        }
        self.chain.append(block)

    def new_block(self):
        previous_block = self.dict_to_hash(self.last_block())
        block = {
            "index": len(self.chain),
            "timestamp": time.time(),
            "transactions": self.current_transactions,
            "previous_hash": previous_block,
        }
        self.chain.append(block)
        self.current_transactions = []

    def new_transaction(self, sender, amount, receiver):
        fees = 0.02
        self.sender = sender
        self.amount = amount
        self.receiver = receiver
        transaction = {
            "sender": self.sender,
            "amount": self.amount,
            "bpsc": "bpsc_wallet_address",
            "amount_bpsc": self.amount * fees,
            "receiver": self.receiver,
            "amount_receiver": amount * (1 - 0.99995),
        }
        self.current_transactions.append(transaction)
        return len(self.chain)

    # @property
    def last_block(self):
        return self.chain[-1]

    # @property
    def last_block_json(self):
        return json.dumps(self.last_block())
