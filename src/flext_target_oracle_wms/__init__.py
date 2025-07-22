"""FLEXT Target Oracle WMS - Oracle WMS Data Loading with simplified imports.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.7.0 - Target Oracle WMS with simplified public API:
- All common imports available from root: from flext_target_oracle_wms import TargetOracleWMS
- Built on flext-core foundation for robust Oracle WMS data loading
- Deprecation warnings for internal imports
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

# Import from flext-core for foundational patterns
from flext_core import BaseConfig, DomainBaseModel
from flext_core.domain.shared_types import ServiceResult

try:
    __version__ = importlib.metadata.version("flext-target-oracle-wms")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.7.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


class FlextTargetOracleWmsDeprecationWarning(DeprecationWarning):
    """Custom deprecation warning for FLEXT TARGET ORACLE WMS import changes."""


def _show_deprecation_warning(old_import: str, new_import: str) -> None:
    """Show deprecation warning for import paths."""
    message_parts = [
        f"⚠️  DEPRECATED IMPORT: {old_import}",
        f"✅ USE INSTEAD: {new_import}",
        "🔗 This will be removed in version 1.0.0",
        "📖 See FLEXT TARGET ORACLE WMS docs for migration guide",
    ]
    warnings.warn(
        "\n".join(message_parts),
        FlextTargetOracleWmsDeprecationWarning,
        stacklevel=3,
    )


# ================================
# SIMPLIFIED PUBLIC API EXPORTS
# ================================

# Foundation patterns - ALWAYS from flext-core
from flext_core import (
    BaseConfig as WMSBaseConfig,  # Configuration base
    DomainBaseModel as BaseModel,  # Base for WMS models
    DomainError as WMSError,  # WMS-specific errors
    ValidationError as ValidationError,  # Validation errors
)

# Singer Target exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_target_oracle_wms.target import TargetOracleWMS

# WMS Client exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_target_oracle_wms.client import (
        WMSAuthenticator,
        WMSClient,
    )

# WMS Sinks exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_target_oracle_wms.sinks import (
        WMSInventorySink,
        WMSLaborSink,
        WMSReceiptSink,
        WMSShipmentSink,
    )

# ================================
# PUBLIC API EXPORTS
# ================================

__all__ = [
    "BaseModel",  # from flext_target_oracle_wms import BaseModel
    # Deprecation utilities
    "FlextTargetOracleWmsDeprecationWarning",
    "ServiceResult",  # from flext_target_oracle_wms import ServiceResult
    # Main Singer Target (simplified access)
    "TargetOracleWMS",  # from flext_target_oracle_wms import TargetOracleWMS
    "ValidationError",  # from flext_target_oracle_wms import ValidationError
    # WMS Authentication (simplified access)
    "WMSAuthenticator",  # from flext_target_oracle_wms import WMSAuthenticator
    # Core Patterns (from flext-core)
    "WMSBaseConfig",  # from flext_target_oracle_wms import WMSBaseConfig
    # WMS Client (simplified access)
    "WMSClient",  # from flext_target_oracle_wms import WMSClient
    "WMSError",  # from flext_target_oracle_wms import WMSError
    # WMS Sinks (simplified access)
    "WMSInventorySink",  # from flext_target_oracle_wms import WMSInventorySink
    "WMSLaborSink",  # from flext_target_oracle_wms import WMSLaborSink
    "WMSReceiptSink",  # from flext_target_oracle_wms import WMSReceiptSink
    "WMSShipmentSink",  # from flext_target_oracle_wms import WMSShipmentSink
    # Version
    "__version__",
    "__version_info__",
]
