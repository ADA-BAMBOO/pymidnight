from pymidnight.tx import Transaction


def test_transaction_to_dict():
    tx = Transaction(
        sender="addr_test1...",
        note_id="note-123",
        metadata="hello world",
        fee=42,
        network_id="devnet",
    )

    d = tx.to_dict()
    assert d["sender"] == "addr_test1..."
    assert d["note_id"] == "note-123"
    assert d["metadata"] == "hello world"
    assert d["fee"] == 42
    assert d["network_id"] == "devnet"
