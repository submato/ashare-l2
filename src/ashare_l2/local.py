"""Read day-partitioned Wind-style L2 CSV folders from disk."""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd

from .schema import CHANNELS, Channel, normalize_channel


def _open_csv(path: Path) -> pd.DataFrame:
    """Wealth / Wind L2 CSVs are typically GBK; fall back to UTF-8."""
    last_err: Exception | None = None
    for enc in ("gbk", "utf-8-sig", "utf-8"):
        try:
            return pd.read_csv(path, encoding=enc)
        except Exception as exc:  # noqa: BLE001 — try next encoding
            last_err = exc
    raise RuntimeError(f"Failed to read {path}") from last_err


class LocalL2Store:
    """Offline store for the unified layout::

        {root}/{symbol}/l2/YYYYMMDD/{行情,逐笔委托,逐笔成交}.csv
    """

    def __init__(self, root: str | Path | None = None) -> None:
        env = os.environ.get("ASHARE_L2_DATA_ROOT")
        self.root = Path(root or env or ".").expanduser().resolve()

    def day_dir(self, symbol: str, day: str) -> Path:
        return self.root / symbol / "l2" / day

    def list_days(self, symbol: str) -> list[str]:
        base = self.root / symbol / "l2"
        if not base.is_dir():
            return []
        return sorted(
            p.name
            for p in base.iterdir()
            if p.is_dir() and p.name.isdigit() and len(p.name) == 8
        )

    def path(self, symbol: str, day: str, channel: str | Channel) -> Path:
        ch = normalize_channel(channel)
        return self.day_dir(symbol, day) / CHANNELS[ch]

    def load(
        self,
        symbol: str,
        day: str,
        channel: str | Channel = "snapshot",
    ) -> pd.DataFrame:
        path = self.path(symbol, day, channel)
        if not path.is_file():
            raise FileNotFoundError(path)
        return _open_csv(path)

    def exists(self, symbol: str, day: str, channel: str | Channel = "snapshot") -> bool:
        return self.path(symbol, day, channel).is_file()
