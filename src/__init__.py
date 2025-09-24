"""FLEXT Oracle WMS Target - Enhanced Oracle WMS target for FLEXT data pipeline.

This package provides comprehensive Oracle WMS target functionality with
enhanced Pydantic 2.11 features, comprehensive validation, and security.
"""

from __future__ import annotations

from .constants import FlextTargetOracleWmsConstants
from .models import FlextTargetOracleWmsModels
from .target_config import FlextTargetOracleWmsConfig

# Re-export main classes for easy access
__all__ = [
    "FlextTargetOracleWmsConfig",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
]

# Package metadata
__version__ = "1.0.0"
__author__ = "FLEXT Team"
__description__ = "Enhanced Oracle WMS target for FLEXT data pipeline"
