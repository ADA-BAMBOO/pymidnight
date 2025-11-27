import typer

from .config import NetworkConfig
from .client import MidnightClient
from .tx import Transaction


app = typer.Typer(help="PyMidnight CLI – demo commands")


def _make_client() -> MidnightClient:
    cfg = NetworkConfig.from_env()
    return MidnightClient(cfg)


@app.command()
def health():
    client = _make_client()
    res = client.get_health()
    typer.echo(f"Health: {res}")


@app.command("demo-store-note")
def demo_store_note(
    note_id: str = typer.Argument(..., help="Note ID to store"),
    metadata: str = typer.Argument(..., help="Note metadata / content"),
):
    client = _make_client()
    tx = Transaction(sender="demo-sender", note_id=note_id, metadata=metadata)
    res = client.call_contract("storeNote", tx.to_dict())
    typer.echo(f"storeNote result: {res}")


@app.command("demo-reveal-note")
def demo_reveal_note(
    note_id: str = typer.Argument(..., help="Note ID to read"),
):
    client = _make_client()
    args = {"note_id": note_id}
    res = client.call_contract("revealNote", args)
    typer.echo(f"revealNote result: {res}")


if __name__ == "__main__":
    app()
