import json
import os
from typing import Dict, List, Optional

from coin import Coin


class JsonDB:

    def __init__(self, filename: str, directory: Optional[str] = None) -> None:
        if directory:
            os.makedirs(directory, exist_ok=True)
            self.filename = os.path.join(directory, filename)
        else:
            self.filename = filename
        self.data: Dict[str, Coin] = {}
        self.load()

    def load(self) -> None:
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                if os.stat(self.filename).st_size == 0:
                    self.data = {}
                else:
                    raw_data = json.load(f)
                    self.data = {k: Coin.from_dict(v) for k, v in raw_data.items()}

    def save(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.data.items()}, f, indent=2)

    def set(self, key: str, value: Coin) -> None:
        if not isinstance(value, Coin):
            raise TypeError("Value must be an instance of Coin")
        self.data[key] = value
        self.save()

    def get(self, key: str, default: Optional[Coin] = None) -> Optional[Coin]:
        return self.data.get(key, default)

    def delete(self, key: str) -> None:
        if key in self.data:
            del self.data[key]
            self.save()

    def all_coins_dict(self) -> Dict[str, Coin]:
        """Return all data in the DB file as a dict of Coin.name: Coin instances."""
        return self.data

    def all_coins_list(self) -> List[Coin]:
        """Return all data in the DB file as a list of Coin instances."""
        return list(self.data.values())
