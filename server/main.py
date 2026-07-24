"""Minimal FastAPI service that serves day-partitioned L2 CSVs.

Run::

    export ASHARE_L2_DATA_ROOT=/path/to/stockdata
    pip install -e '.[server]'
    uvicorn server.main:app --reload --port 8080
"""

from __future__ import annotations

import io
import os
from typing import Literal

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import PlainTextResponse

from ashare_l2.local import LocalL2Store
from ashare_l2.schema import CHANNELS, normalize_channel

app = FastAPI(
    title="A-Share Level-2 Data API",
    description="Serve China A-share Level-2 snapshots, orders, and trades.",
    version="0.1.0",
)

store = LocalL2Store(os.environ.get("ASHARE_L2_DATA_ROOT"))


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "data_root": str(store.root)}


@app.get("/v1/symbols")
def list_symbols() -> dict[str, list[str]]:
    if not store.root.is_dir():
        return {"symbols": []}
    symbols = sorted(
        p.name
        for p in store.root.iterdir()
        if p.is_dir() and (p / "l2").is_dir()
    )
    return {"symbols": symbols}


@app.get("/v1/l2/{symbol}/days")
def list_days(symbol: str) -> dict[str, list[str]]:
    return {"symbol": symbol, "days": store.list_days(symbol)}


@app.get("/v1/l2/{symbol}/{day}/{channel}")
def get_channel(
    symbol: str,
    day: str,
    channel: str,
    format: Literal["json", "csv"] = Query(default="json"),
):
    try:
        ch = normalize_channel(channel)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    if not (day.isdigit() and len(day) == 8):
        raise HTTPException(status_code=400, detail="day must be YYYYMMDD")

    path = store.path(symbol, day, ch)
    if not path.is_file():
        raise HTTPException(
            status_code=404,
            detail=f"missing {CHANNELS[ch]} for {symbol} {day}",
        )

    df = store.load(symbol, day, ch)
    # Drop unnamed trailing columns from Wind exports.
    df = df.loc[:, [c for c in df.columns if not str(c).startswith("Unnamed")]]

    if format == "csv":
        buf = io.StringIO()
        df.to_csv(buf, index=False)
        return PlainTextResponse(buf.getvalue(), media_type="text/csv")

    return {
        "symbol": symbol,
        "day": day,
        "channel": ch,
        "filename": CHANNELS[ch],
        "rows": df.to_dict(orient="records"),
        "count": int(len(df)),
    }
