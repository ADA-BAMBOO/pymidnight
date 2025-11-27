from dataclasses import dataclass
import os


@dataclass
class NetworkConfig:
    base_url: str
    network_id: str = "devnet"
    timeout: float = 10.0

    @classmethod
    def from_env(cls) -> "NetworkConfig":
        base = os.getenv("MIDNIGHT_BASE_URL", "http://localhost:2222")
        nid = os.getenv("MIDNIGHT_NETWORK_ID", "devnet")
        timeout_raw = os.getenv("MIDNIGHT_TIMEOUT", "10")

        try:
            timeout_val = float(timeout_raw)
        except ValueError:
            timeout_val = 10.0

        return cls(base_url=base, network_id=nid, timeout=timeout_val)
