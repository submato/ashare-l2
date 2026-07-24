# ashare-l2 — China A-Share Level-2 Market Data

Python SDK + minimal HTTP API for **China A-share Level-2** data: ten-level order book snapshots, tick-by-tick orders, and tick-by-tick trades.

面向量化研究与交易系统的 A 股 Level-2 数据访问层：十档快照、逐笔委托、逐笔成交。

## Features

- **Three L2 channels**: `snapshot` / `order` / `trade`
- **Day-partitioned layout** compatible with common Wind-style CSV dumps
- **Local reader** (`LocalL2Store`) for offline folders
- **HTTP API** (FastAPI) to serve the same layout over the network
- **Tiny synthetic sample** under `samples/` for smoke tests (not real market data)

## Data layout

```text
{DATA_ROOT}/{SYMBOL}/l2/YYYYMMDD/
  行情.csv        # snapshot
  逐笔委托.csv    # order
  逐笔成交.csv    # trade
```

See [docs/schema.md](docs/schema.md) for field definitions.

## Quick start (local)

```bash
git clone https://github.com/submato/ashare-l2.git
cd ashare-l2
python -m venv .venv && source .venv/bin/activate
pip install -e .

python examples/read_local.py
```

Point the store at your own dump:

```python
from ashare_l2 import LocalL2Store

store = LocalL2Store("/path/to/stockdata")
df = store.load("300476.SZ", "20250102", "snapshot")
print(df.head())
```

## Quick start (HTTP API)

```bash
pip install -e '.[server]'
export ASHARE_L2_DATA_ROOT=./samples
uvicorn server.main:app --reload --port 8080
```

```bash
curl 'http://127.0.0.1:8080/v1/symbols'
curl 'http://127.0.0.1:8080/v1/l2/DEMO.SZ/20250102/snapshot?format=json'
```

API reference: [docs/api.md](docs/api.md)

## Python client

```python
from ashare_l2 import L2Client

client = L2Client(base_url="http://127.0.0.1:8080/v1", api_key="...")
df = client.load_frame("DEMO.SZ", "20250102", "trade")
```

## Project structure

```text
ashare-l2/
  src/ashare_l2/     # SDK: client + local reader + schema
  server/            # FastAPI service
  docs/              # schema & API docs
  examples/          # local / remote usage
  samples/           # synthetic DEMO.SZ day folder
```

## Use cases

- Serve historical L2 day files to research notebooks / agents
- Normalize Wind-style CSVs behind a stable HTTP contract
- Bootstrap T0 / microstructure feature pipelines without wiring vendor SDKs first

## Important notes

- This repository ships **code and schema**, not a full exchange dump.
- Redistribution of real Level-2 history may require exchange / vendor licenses.
- Confirm price scaling (often ×10000 in Wind exports) before trading use.

## License

MIT for source code. Market data itself may have separate terms.

## GitHub topics (suggested)

`china` `a-share` `level2` `market-data` `order-book` `tick-data` `quant` `fastapi` `python` `wind`
