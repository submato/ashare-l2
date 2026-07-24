"""Fetch L2 via HTTP API (requires a running server)."""

import os

from ashare_l2 import L2Client

os.environ.setdefault("ASHARE_L2_BASE_URL", "http://127.0.0.1:8080/v1")

client = L2Client()
print("symbols:", client.list_symbols())
print("days:", client.list_days("DEMO.SZ"))
df = client.load_frame("DEMO.SZ", "20250102", "snapshot")
print(df.head())
