"""Constants for flext_target_oracle_wms._constants.factory."""

from __future__ import annotations

from collections.abc import Mapping

from flext_target_oracle_wms.typings import t

PRESETS: Mapping[str, t.JsonMapping] = {
    "development": {
        "batch_size": 100,
        "timeout": 30,
        "max_retries": 3,
        "verify_ssl": False,
        "enable_logging": True,
    },
    "production": {
        "batch_size": 1000,
        "timeout": 120,
        "max_retries": 10,
        "verify_ssl": True,
        "enable_logging": True,
    },
    "testing": {
        "batch_size": 10,
        "timeout": 15,
        "max_retries": 1,
        "verify_ssl": False,
        "enable_logging": False,
    },
}
