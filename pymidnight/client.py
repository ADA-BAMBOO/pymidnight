import logging
from typing import Any, Dict

from .config import NetworkConfig


logger = logging.getLogger(__name__)


class MidnightClient:
    def __init__(self, config: NetworkConfig) -> None:
        self.config = config

    def get_health(self) -> Dict[str, Any]:
        logger.debug("Mock get_health called")
        return {
            "status": "ok",
            "base_url": self.config.base_url,
            "network_id": self.config.network_id,
        }

    def submit_tx(self, raw_tx: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Mock submit_tx called")
        return {
            "status": "submitted",
            "tx_id": "mock-tx-id",
            "network_id": self.config.network_id,
        }

    def call_contract(self, entrypoint: str, args: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Mock call_contract called")
        return {
            "status": "ok",
            "entrypoint": entrypoint,
            "echo": args,
        }
