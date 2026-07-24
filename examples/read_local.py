"""Read a local day folder with LocalL2Store."""

from pathlib import Path

from ashare_l2 import LocalL2Store

ROOT = Path(__file__).resolve().parents[1] / "samples"
store = LocalL2Store(ROOT)

symbol, day = "DEMO.SZ", "20250102"
print("days:", store.list_days(symbol))

for channel in ("snapshot", "order", "trade"):
    df = store.load(symbol, day, channel)
    print(channel, df.shape)
    print(df.head(2))
    print()
