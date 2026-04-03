# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target oracle wms package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_target_oracle_wms.__version__ import (
    __all__,
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_target_oracle_wms import (
        _utilities,
        api,
        cli,
        client,
        constants,
        factory,
        helpers,
        models,
        protocols,
        service_runtime,
        target_config,
        typings,
        utilities,
    )
    from flext_target_oracle_wms._utilities import (
        CatalogManager,
        FlextTargetOracleWmsServiceRuntime,
        StreamProcessor,
        Target,
        Validation,
        WMSDataTransformer,
        WMSSchemaMapper,
        WMSTableManager,
        WMSTypeConverter,
        create_record_message,
        create_schema_message,
        create_state_message,
    )
    from flext_target_oracle_wms.api import FlextTargetOracleWmsService
    from flext_target_oracle_wms.cli import FlextTargetOracleWmsCli
    from flext_target_oracle_wms.constants import (
        FlextTargetOracleWmsConstants,
        FlextTargetOracleWmsConstants as c,
    )
    from flext_target_oracle_wms.factory import (
        FlextTargetFactory,
        base_url,
        create_monitored_oracle_wms_target,
        environment,
        logger,
        password,
        preset,
        username,
    )
    from flext_target_oracle_wms.models import (
        FlextTargetOracleWmsModels,
        FlextTargetOracleWmsModels as m,
    )
    from flext_target_oracle_wms.protocols import (
        FlextTargetOracleWmsProtocols,
        FlextTargetOracleWmsProtocols as p,
    )
    from flext_target_oracle_wms.target_config import FlextTargetOracleWmsSettings
    from flext_target_oracle_wms.typings import (
        FlextTargetOracleWmsTypes,
        FlextTargetOracleWmsTypes as t,
    )
    from flext_target_oracle_wms.utilities import (
        FlextTargetOracleWmsUtilities,
        FlextTargetOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_target_oracle_wms._utilities",),
    {
        "FlextTargetFactory": "flext_target_oracle_wms.factory",
        "FlextTargetOracleWmsCli": "flext_target_oracle_wms.cli",
        "FlextTargetOracleWmsConstants": "flext_target_oracle_wms.constants",
        "FlextTargetOracleWmsModels": "flext_target_oracle_wms.models",
        "FlextTargetOracleWmsProtocols": "flext_target_oracle_wms.protocols",
        "FlextTargetOracleWmsService": "flext_target_oracle_wms.api",
        "FlextTargetOracleWmsSettings": "flext_target_oracle_wms.target_config",
        "FlextTargetOracleWmsTypes": "flext_target_oracle_wms.typings",
        "FlextTargetOracleWmsUtilities": "flext_target_oracle_wms.utilities",
        "_utilities": "flext_target_oracle_wms._utilities",
        "api": "flext_target_oracle_wms.api",
        "base_url": "flext_target_oracle_wms.factory",
        "c": ("flext_target_oracle_wms.constants", "FlextTargetOracleWmsConstants"),
        "cli": "flext_target_oracle_wms.cli",
        "client": "flext_target_oracle_wms.client",
        "constants": "flext_target_oracle_wms.constants",
        "create_monitored_oracle_wms_target": "flext_target_oracle_wms.factory",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "environment": "flext_target_oracle_wms.factory",
        "factory": "flext_target_oracle_wms.factory",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "helpers": "flext_target_oracle_wms.helpers",
        "logger": "flext_target_oracle_wms.factory",
        "m": ("flext_target_oracle_wms.models", "FlextTargetOracleWmsModels"),
        "models": "flext_target_oracle_wms.models",
        "p": ("flext_target_oracle_wms.protocols", "FlextTargetOracleWmsProtocols"),
        "password": "flext_target_oracle_wms.factory",
        "preset": "flext_target_oracle_wms.factory",
        "protocols": "flext_target_oracle_wms.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "service_runtime": "flext_target_oracle_wms.service_runtime",
        "t": ("flext_target_oracle_wms.typings", "FlextTargetOracleWmsTypes"),
        "target_config": "flext_target_oracle_wms.target_config",
        "typings": "flext_target_oracle_wms.typings",
        "u": ("flext_target_oracle_wms.utilities", "FlextTargetOracleWmsUtilities"),
        "username": "flext_target_oracle_wms.factory",
        "utilities": "flext_target_oracle_wms.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__all__",
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
