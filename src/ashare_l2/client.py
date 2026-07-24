"""HTTP client for the A-share Level-2 data API."""

from __future__ import annotations

import os
from typing import Any

import httpx
import pandas as pd

from .schema import Channel, normalize_channel


class L2Client:
    """Thin client around ``GET /v1/l2/{symbol}/{day}/{channel}``."""

    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        timeout: float = 60.0,
    ) -> None:
        self.base_url = (base_url or os.environ.get("ASHARE_L2_BASE_URL") or "").rstrip("/")
        self.api_key = api_key or os.environ.get("ASHARE_L2_API_KEY")
        self.timeout = timeout
        if not self.base_url:
            raise ValueError(
                "ASHARE_L2_BASE_URL is not set. "
                "Pass base_url=... or use LocalL2Store for offline CSVs."
            )

    def _headers(self) -> dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def get(
        self,
        symbol: str,
        day: str,
        channel: str | Channel = "snapshot",
        *,
        format: str = "json",
    ) -> Any:
        ch = normalize_channel(channel)
        url = f"{self.base_url}/l2/{symbol}/{day}/{ch}"
        with httpx.Client(timeout=self.timeout, headers=self._headers()) as client:
            resp = client.get(url, params={"format": format})
            resp.raise_for_status()
            if format == "csv":
                return resp.text
            return resp.json()

    def load_frame(
        self,
        symbol: str,
        day: str,
        channel: str | Channel = "snapshot",
    ) -> pd.DataFrame:
        payload = self.get(symbol, day, channel, format="json")
        rows = payload.get("rows", payload) if isinstance(payload, dict) else payload
        return pd.DataFrame(rows)

    def list_symbols(self) -> list[str]:
        with httpx.Client(timeout=self.timeout, headers=self._headers()) as client:
            resp = client.get(f"{self.base_url}/symbols")
            resp.raise_for_status()
            data = resp.json()
            return list(data.get("symbols", data))

    def list_days(self, symbol: str) -> list[str]:
        with httpx.Client(timeout=self.timeout, headers=self._headers()) as client:
            resp = client.get(f"{self.base_url}/l2/{symbol}/days")
            resp.raise_for_status()
            data = resp.json()
            return list(data.get("days", data))
