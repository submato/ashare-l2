"""China A-share Level-2 market data client and local reader."""

from .client import L2Client
from .local import LocalL2Store
from .schema import CHANNELS, Channel

__all__ = ["L2Client", "LocalL2Store", "CHANNELS", "Channel"]
__version__ = "0.1.0"
