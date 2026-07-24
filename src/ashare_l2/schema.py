"""Canonical channel names and Wind-style CSV column maps for A-share L2."""

from __future__ import annotations

from typing import Literal

Channel = Literal["snapshot", "order", "trade"]

CHANNELS: dict[Channel, str] = {
    "snapshot": "行情.csv",  # 10-level order book snapshot
    "order": "逐笔委托.csv",  # tick-by-tick order
    "trade": "逐笔成交.csv",  # tick-by-tick trade / cancel
}

# Common Wind / exchange CSV headers (GBK on disk).
SNAPSHOT_COLUMNS = [
    "万得代码",
    "交易所代码",
    "自然日",
    "时间",
    "成交价",
    "成交量",
    "成交额",
    "成交笔数",
    "IOPV",
    "成交标志",
    "BS标志",
    "当日累计成交量",
    "当日成交额",
    "最高价",
    "最低价",
    "开盘价",
    "前收盘",
    *[f"申卖价{i}" for i in range(1, 11)],
    *[f"申卖量{i}" for i in range(1, 11)],
    *[f"申买价{i}" for i in range(1, 11)],
    *[f"申买量{i}" for i in range(1, 11)],
    "加权平均叫卖价",
    "加权平均叫买价",
    "叫卖总量",
    "叫买总量",
]

ORDER_COLUMNS = [
    "万得代码",
    "交易所代码",
    "自然日",
    "时间",
    "委托编号",
    "交易所委托号",
    "委托类型",
    "委托代码",
    "委托价格",
    "委托数量",
]

TRADE_COLUMNS = [
    "万得代码",
    "交易所代码",
    "自然日",
    "时间",
    "成交编号",
    "成交代码",
    "委托代码",
    "BS标志",
    "成交价格",
    "成交数量",
    "叫卖序号",
    "叫买序号",
]

# English aliases used by the HTTP API / SDK.
EN_CHANNEL_ALIASES: dict[str, Channel] = {
    "snapshot": "snapshot",
    "quote": "snapshot",
    "行情": "snapshot",
    "order": "order",
    "orders": "order",
    "逐笔委托": "order",
    "trade": "trade",
    "trades": "trade",
    "逐笔成交": "trade",
}


def normalize_channel(name: str) -> Channel:
    key = name.strip().lower()
    # Keep Chinese names as-is for lookup.
    if name in EN_CHANNEL_ALIASES:
        return EN_CHANNEL_ALIASES[name]
    if key in EN_CHANNEL_ALIASES:
        return EN_CHANNEL_ALIASES[key]
    raise ValueError(f"Unknown L2 channel: {name!r}. Expected one of {list(CHANNELS)}")
