#!/usr/bin/env python3
"""Generate config.json from .env file for target-oracle-wms."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def generate_target_config() -> dict[str, Any]:
    """Generate target configuration from environment variables."""
    config: dict[str, Any] = {
        "base_url": os.getenv("WMS_BASE_URL", "https://test.oracle.com/wms/api/v1"),
        "username": os.getenv("WMS_USERNAME", "test_user"),
        "password": os.getenv("WMS_PASSWORD", "test_password"),
        "timeout": int(os.getenv("WMS_TIMEOUT", "300")),
        "enable_kpi_calculation": os.getenv("WMS_ENABLE_KPI", "true").lower() == "true",
        "enable_alerts": os.getenv("WMS_ENABLE_ALERTS", "true").lower() == "true",
        "expiry_alert_days": int(os.getenv("WMS_EXPIRY_ALERT_DAYS", "30")),
        "output_path": os.getenv("WMS_OUTPUT_PATH", "./output"),
        "output_format": os.getenv("WMS_OUTPUT_FORMAT", "json"),
    }

    # Add database URL if provided
    db_url = os.getenv("WMS_DATABASE_URL")
    if db_url:
        config["database_url"] = db_url

    # Add webhook URL if provided
    webhook_url = os.getenv("WMS_ALERT_WEBHOOK_URL")
    if webhook_url:
        config["alert_webhook_url"] = webhook_url

    # Add test mode flag
    if os.getenv("WMS_TEST_MODE", "false").lower() == "true":
        config["test_mode"] = True

    return config


def main() -> None:
    """Generate config.json file."""
    config_path = Path("config.json")

    if config_path.exists():
        config_path.rename("config.json.bak")

    config = generate_target_config()

    config_path.write_text(json.dumps(config, indent=2))


if __name__ == "__main__":
    main()
