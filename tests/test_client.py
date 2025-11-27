from pymidnight.config import NetworkConfig
from pymidnight.client import MidnightClient


def make_client() -> MidnightClient:
    cfg = NetworkConfig(base_url="http://localhost:8080", network_id="devnet", timeout=5.0)
    return MidnightClient(cfg)


def test_get_health_mock():
    client = make_client()
    res = client.get_health()
    assert res["status"] == "ok"
    assert res["base_url"] == "http://localhost:2222"
    assert res["network_id"] == "devnet"


def test_submit_tx_mock():
    client = make_client()
    raw_tx = {"foo": "bar"}
    res = client.submit_tx(raw_tx)
    assert res["status"] == "submitted"
    assert res["tx_id"] == "mock-tx-id"
    assert res["network_id"] == "devnet"


def test_call_contract_mock():
    client = make_client()
    args = {"note_id": "n1"}
    res = client.call_contract("storeNote", args)
    assert res["status"] == "ok"
    assert res["entrypoint"] == "storeNote"
    assert res["echo"] == args
