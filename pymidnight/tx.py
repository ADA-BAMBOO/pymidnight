from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class Transaction:
    sender: str
    note_id: str
    metadata: str
    fee: int = 0
    network_id: str = "devnet"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
