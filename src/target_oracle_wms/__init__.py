"""Target for Oracle Warehouse Management System."""

from __future__ import annotations

from target_oracle_wms.__version__ import __version__
from target_oracle_wms.target import TargetOracleWMS

__all__ = ["TargetOracleWMS", "__version__"]
