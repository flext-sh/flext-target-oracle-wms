"""Pytest configuration for target-oracle-wms tests.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

# PYTHON_VERSION_GUARD — Do not remove. Managed by scripts/maintenance/enforce_python_version.py
import sys as _sys

if _sys.version_info[:2] != (3, 13):
    _v = (
        f"{_sys.version_info.major}.{_sys.version_info.minor}.{_sys.version_info.micro}"
    )
    raise RuntimeError(
        f"\n{'=' * 72}\n"
        f"FATAL: Python {_v} detected — this project requires Python 3.13.\n"
        f"\n"
        f"The virtual environment was created with the WRONG Python interpreter.\n"
        f"\n"
        f"Fix:\n"
        f"  1. rm -rf .venv\n"
        f"  2. poetry env use python3.13\n"
        f"  3. poetry install\n"
        f"\n"
        f"Or use the workspace Makefile:\n"
        f"  make setup PROJECT=<project-name>\n"
        f"{'=' * 72}\n"
    )
del _sys
# PYTHON_VERSION_GUARD_END

import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest
from flext_core import FlextTypes as t


@pytest.fixture
def config() -> dict[str, t.GeneralValueType]:
    """Return a test configuration."""
    return {
        "base_url": "https://test.oracle.com/wms/api/v1",
        "username": "test_user",
        "password": "test_pass",
        "timeout": 30,
        "enable_kpi_calculation": True,
        "enable_alerts": True,
        "expiry_alert_days": 30,
        "output_path": "./test_output",
        "output_format": "json",
    }


@pytest.fixture
def temp_output_dir() -> Generator[Path]:
    """Create a temporary output directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_inventory_records() -> list[dict[str, t.GeneralValueType]]:
    """Return sample inventory records."""
    return [
        {
            "item_id": "ITEM001",
            "item_description": "Test Item 1",
            "quantity": 100,
            "location": "A-01-01",
            "lot_number": "LOT001",
            "expiry_date": "2024-12-31",
            "unit_cost": 10.50,
        },
        {
            "item_id": "ITEM002",
            "item_description": "Test Item 2",
            "quantity": 50,
            "location": "A-01-02",
            "lot_number": "LOT002",
            "expiry_date": "2024-06-30",
            "unit_cost": 25.00,
        },
    ]


@pytest.fixture
def sample_order_records() -> list[dict[str, t.GeneralValueType]]:
    """Return sample order records."""
    return [
        {
            "order_id": "ORD001",
            "customer_id": "CUST001",
            "order_date": "2024-01-01T10:00:00Z",
            "status": "SHIPPED",
            "total_amount": 1000.00,
            "ship_date": "2024-01-02T15:00:00Z",
        },
        {
            "order_id": "ORD002",
            "customer_id": "CUST002",
            "order_date": "2024-01-02T11:00:00Z",
            "status": "PENDING",
            "total_amount": 500.00,
            "ship_date": None,
        },
    ]


@pytest.fixture
def sample_task_records() -> list[dict[str, t.GeneralValueType]]:
    """Return sample task records."""
    return [
        {
            "task_id": "TASK001",
            "task_type": "PICK",
            "worker_id": "WORK001",
            "status": "COMPLETED",
            "start_time": "2024-01-01T08:00:00Z",
            "end_time": "2024-01-01T08:30:00Z",
            "items_processed": 50,
        },
        {
            "task_id": "TASK002",
            "task_type": "PACK",
            "worker_id": "WORK002",
            "status": "IN_PROGRESS",
            "start_time": "2024-01-01T09:00:00Z",
            "end_time": None,
            "items_processed": 25,
        },
    ]


@pytest.fixture
def singer_schema() -> dict[str, t.GeneralValueType]:
    """Return a sample Singer schema."""
    return {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "quantity": {"type": "integer"},
            "price": {"type": "number"},
            "updated_at": {"type": "string", "format": "date-time"},
        },
    }
