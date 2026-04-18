"""Blockchain-based supply chain."""
import hashlib
import json
from datetime import datetime
from typing import Dict, List

class SupplyChain:
    """Track supply chain on blockchain."""
    
    def __init__(self):
        self.chain = []
        self._add_genesis()
    
    def _add_genesis(self):
        self.chain.append({'index': 0, 'hash': '0', 'data': 'Genesis'})
    
    def add_event(self, product_id: str, event: str, location: str):
        block = {
            'index': len(self.chain),
            'timestamp': datetime.now().isoformat(),
            'product_id': product_id,
            'event': event,
            'location': location,
            'previous_hash': self.chain[-1]['hash']
        }
        block['hash'] = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
        self.chain.append(block)
        return block
    
    def get_history(self, product_id: str) -> List[Dict]:
        return [b for b in self.chain if b.get('product_id') == product_id]
