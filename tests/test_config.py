from pymidnight.config import NetworkConfig


def test_network_config_manual_init():
    cfg = NetworkConfig(base_url="http://example.com", network_id="testnet", timeout=5.0)
    assert cfg.base_url == "http://example.com"
    assert cfg.network_id == "testnet"
    assert cfg.timeout == 5.0


def test_network_config_from_env(monkeypatch):
    monkeypatch.setenv("MIDNIGHT_BASE_URL", "http://test.local:9000")
    monkeypatch.setenv("MIDNIGHT_NETWORK_ID", "devnet-1")
    monkeypatch.setenv("MIDNIGHT_TIMEOUT", "12.5")

    cfg = NetworkConfig.from_env()
    assert cfg.base_url == "http://test.local:9000"
    assert cfg.network_id == "devnet-1"
    assert cfg.timeout == 12.5


def test_network_config_from_env_invalid_timeout(monkeypatch):
    monkeypatch.setenv("MIDNIGHT_TIMEOUT", "not-a-number")

    cfg = NetworkConfig.from_env()
    assert cfg.timeout == 10.0
