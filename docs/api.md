# HTTP API

Base path: `/v1`  
Auth (production): `Authorization: Bearer <ASHARE_L2_API_KEY>`

## Endpoints

### `GET /health`

Service liveness and configured data root.

### `GET /v1/symbols`

List symbols that have an `l2/` directory under the data root.

```json
{ "symbols": ["300476.SZ"] }
```

### `GET /v1/l2/{symbol}/days`

List available `YYYYMMDD` folders for a symbol.

```json
{ "symbol": "300476.SZ", "days": ["20250102", "20250103"] }
```

### `GET /v1/l2/{symbol}/{day}/{channel}`

Fetch one channel for one trade date.

Path params:

- `symbol` — e.g. `300476.SZ`
- `day` — `YYYYMMDD`
- `channel` — `snapshot` | `order` | `trade` (aliases: `行情`, `逐笔委托`, `逐笔成交`)

Query:

- `format=json` (default) or `format=csv`

JSON response shape:

```json
{
  "symbol": "300476.SZ",
  "day": "20250102",
  "channel": "snapshot",
  "filename": "行情.csv",
  "count": 4826,
  "rows": [ { "...": "..." } ]
}
```

## Local demo

```bash
export ASHARE_L2_DATA_ROOT=./samples
pip install -e '.[server]'
uvicorn server.main:app --reload --port 8080

curl 'http://127.0.0.1:8080/v1/l2/DEMO.SZ/20250102/snapshot?format=json'
```
