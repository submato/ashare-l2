# A-Share Level-2 Schema

This project uses a **day-partitioned Wind-style CSV layout**. Encoding on disk is usually **GBK**.

## Directory layout

```text
{DATA_ROOT}/
  {SYMBOL}/                 # e.g. 300476.SZ
    l2/
      YYYYMMDD/
        行情.csv            # 10-level order book snapshot
        逐笔委托.csv        # tick-by-tick orders
        逐笔成交.csv        # tick-by-tick trades / cancels
```

## Channels

| Channel (API) | Filename     | Description                          |
|---------------|--------------|--------------------------------------|
| `snapshot`    | `行情.csv`   | ~3s ten-level bid/ask book + last    |
| `order`       | `逐笔委托.csv` | Every new order / cancel order event |
| `trade`       | `逐笔成交.csv` | Every trade and cancel record        |

## Snapshot (`行情.csv`) — key fields

| Field | Meaning |
|-------|---------|
| 万得代码 | Wind code, e.g. `300476.SZ` |
| 自然日 | Trade date `YYYYMMDD` |
| 时间 | Exchange time, e.g. `91500000` = 09:15:00.000 |
| 成交价 / 成交量 / 成交额 | Last trade fields on the snapshot |
| 申买价1..10 / 申买量1..10 | Bid price / size levels 1–10 |
| 申卖价1..10 / 申卖量1..10 | Ask price / size levels 1–10 |
| 前收盘 / 开盘价 / 最高价 / 最低价 | Daily OHLC reference fields |

Prices in Wind L2 dumps are often stored as **integer × 10000** (e.g. `420900` → `42.09`). Confirm with your vendor feed before using as yuan.

## Order (`逐笔委托.csv`) — key fields

| Field | Meaning |
|-------|---------|
| 交易所委托号 | Exchange order id |
| 委托代码 | Side / type code (`B` / `S`, vendor-specific) |
| 委托价格 | Limit price |
| 委托数量 | Order size (shares) |
| 委托类型 | Order type code (vendor-specific) |

## Trade (`逐笔成交.csv`) — key fields

| Field | Meaning |
|-------|---------|
| 成交编号 | Trade / event id |
| 成交代码 | `0` trade / `C` cancel (vendor-specific) |
| BS标志 | Aggressor side when available |
| 成交价格 / 成交数量 | Trade price / size |
| 叫卖序号 / 叫买序号 | Linked ask / bid order ids |

## Notes

- Do **not** commit full historical dumps into git; keep them under `ASHARE_L2_DATA_ROOT`.
- SZ and SH field nuances may differ slightly by vendor; normalize in your research pipeline.
- Auction window (09:15–09:25) and continuous session should be handled explicitly by consumers.
