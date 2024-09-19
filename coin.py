from typing import Dict, List, Any, Optional


class Coin:

    def __init__(self, name: str, on_work: bool, purchase_amount_KRW: int, split_records: Optional[List[Dict[str, Any]]] = None) -> None:
        self.name: str = name
        self.on_work: bool = on_work
        self.purchase_amount_KRW: int = purchase_amount_KRW
        self.split_records: List[Dict[str, Any]] = split_records or []

    def add_split_record(self, avg_buy_price: float, balance: float) -> None:
        self.split_records.append({
            'avg_buy_price': avg_buy_price,
            'balance': balance
        })

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'on_work': self.on_work,
            'purchase_amount_KRW': self.purchase_amount_KRW,
            'split_records': self.split_records
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Coin':
        return cls(data['name'], data['on_work'], data['purchase_amount_KRW'], data['split_records'])
