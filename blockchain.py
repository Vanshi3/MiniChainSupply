import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(product="Genesis Block", location="Origin", actor="System")

    def create_block(self, product, location, actor):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'product': product,
            'location': location,
            'actor': actor,
            'previous_hash': self.hash(self.chain[-1]) if self.chain else '0'
        }
        self.chain.append(block)
        return block

    def get_chain(self):
        return self.chain

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
