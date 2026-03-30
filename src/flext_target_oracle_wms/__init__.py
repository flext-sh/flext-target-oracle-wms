# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext Target Oracle WMS - Oracle WMS Target Client for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_target_oracle_wms._utilities import _LAZY_IMPORTS as _CHILD_LAZY_0

if TYPE_CHECKING:
    from flext_target_oracle_wms.__version__ import *
    from flext_target_oracle_wms._utilities import *
    from flext_target_oracle_wms.cli import *
    from flext_target_oracle_wms.constants import *
    from flext_target_oracle_wms.factory import *
    from flext_target_oracle_wms.models import *
    from flext_target_oracle_wms.protocols import *
    from flext_target_oracle_wms.target_config import *
    from flext_target_oracle_wms.typings import *
    from flext_target_oracle_wms.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    **_CHILD_LAZY_0,
    "FlextTargetFactory": "flext_target_oracle_wms.factory",
    "FlextTargetMonitoringFactory": "flext_target_oracle_wms.factory",
    "FlextTargetOracleWmsCli": "flext_target_oracle_wms.cli",
    "FlextTargetOracleWmsConstants": "flext_target_oracle_wms.constants",
    "FlextTargetOracleWmsModels": "flext_target_oracle_wms.models",
    "FlextTargetOracleWmsProtocols": "flext_target_oracle_wms.protocols",
    "FlextTargetOracleWmsSettings": "flext_target_oracle_wms.target_config",
    "FlextTargetOracleWmsTypes": "flext_target_oracle_wms.typings",
    "FlextTargetOracleWmsUtilities": "flext_target_oracle_wms.utilities",
    "MIN_CONFIG_ARG_COUNT": "flext_target_oracle_wms.cli",
    "__author__": "flext_target_oracle_wms.__version__",
    "__author_email__": "flext_target_oracle_wms.__version__",
    "__description__": "flext_target_oracle_wms.__version__",
    "__license__": "flext_target_oracle_wms.__version__",
    "__title__": "flext_target_oracle_wms.__version__",
    "__url__": "flext_target_oracle_wms.__version__",
    "__version__": "flext_target_oracle_wms.__version__",
    "__version_info__": "flext_target_oracle_wms.__version__",
    "_utilities": "flext_target_oracle_wms._utilities",
    "c": ["flext_target_oracle_wms.constants", "FlextTargetOracleWmsConstants"],
    "cli": "flext_target_oracle_wms.cli",
    "constants": "flext_target_oracle_wms.constants",
    "create_monitored_oracle_wms_target": "flext_target_oracle_wms.factory",
    "create_oracle_wms_target": "flext_target_oracle_wms.factory",
    "d": "flext_meltano",
    "e": "flext_meltano",
    "factory": "flext_target_oracle_wms.factory",
    "h": "flext_meltano",
    "m": ["flext_target_oracle_wms.models", "FlextTargetOracleWmsModels"],
    "main": "flext_target_oracle_wms.cli",
    "models": "flext_target_oracle_wms.models",
    "p": ["flext_target_oracle_wms.protocols", "FlextTargetOracleWmsProtocols"],
    "protocols": "flext_target_oracle_wms.protocols",
    "r": "flext_meltano",
    "s": "flext_meltano",
    "t": ["flext_target_oracle_wms.typings", "FlextTargetOracleWmsTypes"],
    "target_config": "flext_target_oracle_wms.target_config",
    "typings": "flext_target_oracle_wms.typings",
    "u": ["flext_target_oracle_wms.utilities", "FlextTargetOracleWmsUtilities"],
    "utilities": "flext_target_oracle_wms.utilities",
    "x": "flext_meltano",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
